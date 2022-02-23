import math

from models import GeoLocation


def get_distance_between_points(origin: 'GeoLocation', destination: 'GeoLocation'):
    """
    Calculate the Haversine distance.
    https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

    Parameters
    ----------
    origin : GeoLocation
    destination : GeoLocation

    Returns
    -------
    distance_in_meters : float
    """
    lat1, lon1 = origin.get_lat(), origin.get_long()
    lat2, lon2 = destination.get_lat(), destination.get_long()
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c * 1000
    return distance
