import datetime
import json
import logging
import os

# import gevent
import redis
from flask import Blueprint, jsonify, render_template, request
from pymongo import GEO2D

from direction_service import get_google_direction
from helper import evaluate_formula
from models import DriverPosition, GeoEstimation, GeoLocation

# from flask_sockets import Sockets


fontend_app = Blueprint(__name__, __name__, template_folder='../templates')
ws_app = Blueprint('ws', __name__)

FARE_ESTIMATION_FORMUL = "(time + distance) * 1.5"


from models import Driver, GeoLocation, Pessenger, Trip
from repositories import (DriverPositionRepository, DriverRepository,
                          PessengerRepository, TripRepository)

driver_repository = DriverRepository()
pessenger_repository = PessengerRepository()
trip_repository = TripRepository()
driver_position_repository = DriverPositionRepository()

@fontend_app.route("/", methods=['GET'])
def route_index():
    return jsonify(message="You can run the apis given in the ccurl.md file in postman")


@fontend_app.route("/pessenger/register", methods=['post'])
def route_post_pessenger_register():
    body = request.get_json()
    pessenger = Pessenger(
        name=body['name'],
        email=body['email']
    )
    pessenger_repository.create_entity(pessenger)
    return jsonify(pessenger.to_json())

@fontend_app.route("/driver/register", methods=['post'])
def route_post_driver_register():
    body = request.get_json()
    driver = Driver(
        name=body['name'],
        email=body['email']
    )
    driver_repository.create_entity(driver)
    return jsonify(driver.to_json())

@fontend_app.route("/pessenger/trips", methods=['GET'])
def route_get_pessenger_trips():
    pessenger = pessenger_repository.get_by_id(request.args['pessenger_id'])
    trips = trip_repository.get_by_filters({'pessenger._id': pessenger.get_id()})
    response = [trip.to_json() for trip in trips]
    return jsonify(trips=response)


@fontend_app.route("/customer/create-trip", methods=['POST'])
def route_customer_create_trip():
    body = request.get_json()
    pessenger = pessenger_repository.get_by_id(body['pessenger_id'])
    pickup_location = GeoLocation(
        body['pickup_lat'],
        body['pickup_long']
    )
    destination_location = GeoLocation(
        body['destination_lat'],
        body['destination_long']
    )
    trip = Trip(
        pessenger=pessenger,
        pickup_location=pickup_location,
        destination_location=destination_location
    )
    trip_repository.create_entity(trip)
    dispatch_trip_to_drivers(trip)
    return jsonify(trip=trip.to_json())

def dispatch_trip_to_drivers(trip):
    filters = {}
    drivers = driver_position_repository.filter_by_radial_distance(
        trip.pickup_location,
        filters
    )
    # send the message to driver through socket io
    return drivers


@fontend_app.route("/clear-all", methods=['GET'])
def route_clear_all():
    pessenger_repository.remove_all()
    driver_repository.remove_all()
    trip_repository.remove_all()
    trip_repository.remove_all()
    driver_position_repository.get_collection().create_index([("position", GEO2D)])
    return jsonify(done=True)


@fontend_app.route("/customer/check-price", methods=['POST'])
def route_customer_check_price():
    body = request.get_json()
    pessenger = pessenger_repository.get_by_id(body['pessenger_id'])
    pickup_location = GeoLocation(
        body['pickup_lat'],
        body['pickup_long']
    )
    destination_location = GeoLocation(
        body['destination_lat'],
        body['destination_long']
    )
    price_estimation = get_google_direction(pickup_location, destination_location)

    price_estimation.price = evaluate_formula(
        FARE_ESTIMATION_FORMUL,
        price_estimation.get_distance_in_meters(),
        price_estimation.get_time_in_seconds()
    )
    return jsonify(price_estimation.to_json())


@fontend_app.route("/driver/position", methods=['PUT'])
def route_put_driver_position():
    body = request.get_json()
    driver_current_location = GeoLocation(
        body['location_lat'],
        body['location_long']
    )
    driverPosition = DriverPosition(
        driver_id=body['driver_id'],
        position=driver_current_location
    )
    driver_position_repository.upsert_entity(driverPosition)
    return jsonify(driverPosition.to_json())

def get_driver_positions():
    driver_positions = driver_position_repository.get_by_filters({})
    return driver_positions


@fontend_app.route("/socket-frontend", methods=['GET'])
def route_socker_client():
    context = dict(
        # socket_host_url=os.environ.get('SOCKET_HOST_URL')
        # socket_host_url="ws://localhost/echo",
        driverList=get_driver_positions()
    )
    return render_template('socker-client-page.html', **context)
