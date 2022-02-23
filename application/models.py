from datetime import datetime, timedelta

from bson import json_util
from bson.objectid import ObjectId


class GeoLocation:
    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def get_lat(self):
        return self.latitude

    def get_long(self):
        return self.longitude

    def export_to_mongo(self):
        return self.to_dict()

    def import_from_mongo(self, json_data):
        if json_data:
            self.latitude = json_data.get("latitude", 0.0)
            self.longitude = json_data.get("longitude", 0.0)

    def to_dict(self):
        return {
            'latitude': self.latitude, 
            'longitude': self.longitude
        }

    def to_json(self):
        return self.to_dict()


class GeoEstimation:
    def __init__(self, origin: 'GeoLocation', destination: 'GeoLocation', time_in_seconds=0, distance_in_meters=0, price=0):
        self.origin = origin or GeoLocation()
        self.destination = destination or GeoLocation()
        self.time_in_seconds = int(time_in_seconds)
        self.distance_in_meters = int(distance_in_meters)
        self.price = float(price)

    def get_origin(self):
        return self.origin

    def get_destination(self):
        return self.destination

    def get_time_in_seconds(self):
        return self.time_in_seconds

    def get_time_in_minutes(self):
        return round(self.time_in_seconds / 60, 2)

    def get_distance_in_meters(self):
        return self.distance_in_meters

    def get_distance_in_km(self):
        return round(self.distance_in_meters / 1000, 2)

    def get_price(self):
        return round(self.price, 2)

    def to_dict(self):
        return {
            'origin': self.origin.to_dict(),
            'destination': self.destination.to_dict(),
            'time_in_seconds': self.get_time_in_seconds(),
            'distance_in_meters': self.get_distance_in_meters(),
            'price': self.price,
        }

    def to_json(self):
        return {
            'origin': self.origin.to_json(),
            'destination': self.destination.to_json(),
            'time_in_seconds': self.get_time_in_seconds(),
            'distance_in_meters': self.get_distance_in_meters(),
            'price': self.price,
        }

    def export_to_mongo(self):
        return self.to_dict()

    def import_from_mongo(self, json_data):
        if json_data:
            self.origin.import_from_mongo(json_data.get('origin'))
            self.destination.import_from_mongo(json_data.get('destination'))
            self.time_in_seconds = json_data.get('time_in_seconds', 0)
            self.distance_in_meters = json_data.get('distance_in_meters', 0)
            self.price = json_data.get('price', 0)

class Pessenger(object):
    """A class for storing trip details"""

    def __init__(self, **kwargs):
        pessenger_id = kwargs.get('pessenger_id')
        if pessenger_id is None:
            self._id = ObjectId()
        else:
            self._id = ObjectId(pessenger_id)
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.created_at = kwargs.get('created_at', datetime.today())
        # add some others fields

    def get_id(self):
        return ObjectId(self._id)

    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at,
        }

    def to_json(self):
        return {
            'id': str(self._id),
            'name': self.name,
            'email': self.email,
            'created_at': str(self.created_at),
        }

    def export_to_mongo(self):
        return self.to_dict()

    def import_from_mongo(self, json_data):
        if json_data:
            self._id = json_data.get("_id")
            self.name = json_data.get("name")
            self.email = json_data.get("email")
            self.created_at = json_data.get("created_at")
        return self


class Driver(object):
    """A class for storing driver details"""

    def __init__(self, **kwargs):
        driver_id = kwargs.get('driver_id')
        if driver_id:
            self._id = ObjectId(driver_id)
        else:
            self._id = None
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.created_at = kwargs.get('created_at')

    def get_id(self):
        return ObjectId(self._id)

    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at,
        }

    def to_json(self):
        return {
            'id': str(self._id),
            'name': self.name,
            'email': self.email,
            'created_at': str(self.created_at),
        }

    def export_to_mongo(self):
        return self.to_dict()

    def import_from_mongo(self, json_data):
        if json_data:
            self._id = json_data.get("_id")
            self.name = json_data.get("name")
        return self

class DriverPosition(object):
    """A class for storing driver position in memory db"""

    def __init__(self, **kwargs):
        driver_id = kwargs.get('driver_id')
        if driver_id is None:
            self._id = ObjectId()
        else:
            self._id = ObjectId(driver_id)
        if isinstance(kwargs.get('position'), GeoLocation):
            self.position = kwargs.get('position')
        else:
            self.position = GeoLocation()

    def get_id(self):
        return ObjectId(self._id)

    def to_dict(self):
        return {
            '_id': self._id,
            'position': self.position.to_dict(),
        }

    def to_json(self):
        return {
            'id': str(self._id),
            'position': self.position.to_json(),
        }

    def export_to_mongo(self):
        return {
            '_id': self._id,
            'position': self.position.export_to_mongo(),
        }

    def import_from_mongo(self, json_data):
        if json_data:
            self._id = json_data.get("_id")
            self.position.import_from_mongo(json_data.get('position'))
        return self


class Trip(object):
    """A class for storing trip details"""

    def __init__(self, **kwargs):
        trip_id = kwargs.get('trip_id')
        if trip_id is None:
            self._id = ObjectId()
        else:
            self._id = trip_id
        if isinstance(kwargs.get('pickup_location'), GeoLocation):
            self.pickup_location = kwargs.get('pickup_location')
        else:
            self.pickup_location = GeoLocation()

        if isinstance(kwargs.get('destination_location'), GeoLocation):
            self.destination_location = kwargs.get('destination_location')
        else:
            self.destination_location = GeoLocation()

        if isinstance(kwargs.get('pessenger'), Pessenger):
            self.pessenger = kwargs.get('pessenger')
        else:
            self.pessenger = Pessenger()
    
        if isinstance(kwargs.get('driver'), Driver):
            self.driver = kwargs.get('driver')
        else:
            self.driver = Driver()

        if isinstance(kwargs.get('created_at'), datetime):
            self.created_at = kwargs.get('created_at')
        else:
            self.created_at = datetime.utcnow()

    def get_id(self):
        return ObjectId(self._id)

    def to_dict(self):
        return {
            '_id': self._id,
            'pickup_location': self.pickup_location.export_to_mongo(),
            'destination_location': self.destination_location.export_to_mongo(),
            'pessenger': self.pessenger.export_to_mongo(),
            'driver': self.driver.export_to_mongo(),
            'created_at': self.created_at,
        }

    def to_json(self):
        return {
            'id': str(self._id),
            'pickup_location': self.pickup_location.to_json(),
            'destination_location': self.destination_location.to_json(),
            'pessenger': self.pessenger.to_json(),
            'driver': self.driver.to_json(),
            'created_at': str(self.created_at),
        }

    def export_to_mongo(self):
        return self.to_dict()

    def import_from_mongo(self, json_data):
        if json_data:
            self._id = json_data.get("_id")
            self.pickup_location.import_from_mongo(json_data.get('pickup_location'))
            self.destination_location.import_from_mongo(json_data.get('destination_location'))
            self.pessenger.import_from_mongo(json_data.get('pessenger'))
            self.driver.import_from_mongo(json_data.get('driver'))
            self.city_id = json_data.get("city_id")
            self.created_at = json_data.get("created_at")
        return self
