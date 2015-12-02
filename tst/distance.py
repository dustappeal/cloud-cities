import unittest
from src.distance import distance

class DistanceTests(unittest.TestCase):

    def test_sydney_to_hobart(self):
        dist = distance(-42.87936, 147.32941, -33.86785, 151.20732)
        self.assertEqual(dist, 1057)
        
    def test_sydney_to_seattle(self):
        dist = distance(47.60621, -122.33207, -33.86785, 151.20732)
        self.assertEqual(dist, 12470)

    def test_dublin_to_frankfurt(self):
        dist = distance(53.33306, -6.24889, 50.11552, 8.68417)
        self.assertEqual(dist, 1086)


