

from bson.objectid import ObjectId
from pymongo.collection import Collection

from models import DriverPosition, GeoEstimation, GeoLocation, Pessenger, Trip
from mongo_helper import get_mongo_common_db, get_mongo_mem_db


class MongoBaseRepository(object):
    """Repository trips collection in MongoDB"""

    def __init__(self, collection: 'pymongo.collection.Collection'):
        self.collection = collection
        self.entity_class = None

    def get_by_id(self, doc_id):
        doc = self.collection.find_one({"_id": ObjectId(doc_id)})
        if doc:
            return self.entity_class().import_from_mongo(doc)
        return None
    
    def get_by_filters(self, filters):
        docs = self.collection.find(filters)
        entity_list = []
        for doc in docs:
            entity_list.append(self.entity_class().import_from_mongo(doc))
        return entity_list

    def create_entity(self, entity):
        if entity._id is None:
            entity._id = ObjectId()
        self.collection.insert_one(entity.export_to_mongo())
        return entity

    def update_entity(self, entity, upsert=False):
        updates = entity.export_to_mongo()
        if not upsert:
            del updates['_id']
        result = self.collection.update_one(
            {'_id': entity.get_id()},
            {"$set": updates},
            upsert=True
        )
        return entity

    def upsert_entity(self, entity):
        self.update_entity(entity, True)
        return entity

    def remove_all(self):
        self.collection.delete_many({})

    def get_collection(self):
        return self.collection

class PessengerRepository(MongoBaseRepository):
    """ Repository pessenger collection"""

    def __init__(self):
        database = get_mongo_common_db()
        super().__init__(database.pessengers)
        self.entity_class = Pessenger

class DriverRepository(MongoBaseRepository):
    """ Repository driver collection"""

    def __init__(self):
        database = get_mongo_common_db()
        super().__init__(database.drivers)
        self.entity_class = DriverPosition

class DriverPositionRepository(MongoBaseRepository):
    """ Repository driver position collection"""

    def __init__(self):
        database = get_mongo_mem_db()
        super().__init__(database.driver_position_mem)
        self.entity_class = DriverPosition

    def filter_by_radial_distance(self, pickup_location: 'GeoLocation', filters):
        pipeline = [{
            "$geoNear": {
                "near": [pickup_location.get_lat(), pickup_location.get_long()],
                "distanceField": "radial_distance",
                "spherical": True,
            },
        },
        {
            "$limit": 2,
        }]
        command_result = self.collection.aggregate(pipeline)
        command_result = list(command_result)
        # print(command_result, type(command_result))
        entity_list = []
        for doc in command_result:
            entity_list.append(self.entity_class().import_from_mongo(doc))
        return entity_list

class TripRepository(MongoBaseRepository):
    """ Repository trips collection"""

    def __init__(self):
        database = get_mongo_common_db()
        super().__init__(database.trips)
        self.entity_class = Trip
