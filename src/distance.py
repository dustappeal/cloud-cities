from math import asin
from math import atan
from math import cos
from math import radians
from math import sin
from math import sqrt

RADIUS = 6371 # radius of earth in (km)
PI_DEGREES = 180

def distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two lat/long coordinates, formula from:
    http://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates
    Returns the distance in km.
    """
    assert -90 < lat1 < 90
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    diff_lat = lat2 - lat1
    diff_lon = lon2 - lon1
    a = sin(diff_lat/2)**2 + cos(lat1) * cos(lat2) * sin(diff_lon/2)**2
    c = 2 * asin(sqrt(a))
    return int(c * RADIUS)


