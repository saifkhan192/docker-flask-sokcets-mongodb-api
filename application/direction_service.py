import json
import os

import requests

from geo_helper import get_distance_between_points
from models import GeoEstimation, GeoLocation


def get_google_direction(origin: 'GeoLocation', destination: 'GeoLocation', use_cache=False) -> 'GeoEstimation':
    """
    call google to get the time and distance b/w the given two locations
        ref: https://developers.google.com/maps/documentation/javascript/directions#DirectionsResults
        if GOOGLE_DIRECTION_API_KEY is not set in ENV then this function will calculate on radial distance
    """
    api_key = os.environ.get('GOOGLE_DIRECTION_API_KEY')
    if not api_key:
        distance_in_meters = get_distance_between_points(origin, destination)
        time_in_seconds = (distance_in_meters) / 10
        return GeoEstimation(origin, destination, time_in_seconds, distance_in_meters)
    request_url = 'https://maps.googleapis.com/maps/api/directions/json?key=%s&origin=%s,%s&destination=%s,%s'
    request_url = request_url % (
        origin.get_lat(), origin.get_long(),
        destination.get_lat(), destination.get_long(),
        api_key
    )
    response = requests.request("GET", request_url)
    response_json = response.json()
    time_in_seconds = 0
    distance_in_meters = 0
    if 'routes' in response_json and len(response_json['routes']) > 0:
        paths = response_json['routes'][0]['legs']
        # print(json.dumps(paths[0], indent=3))
        # print(paths)
        time_in_seconds = paths[0]['duration']['value']
        distance_in_meters = paths[0]['distance']['value']
    return GeoEstimation(origin, destination, time_in_seconds, distance_in_meters)
