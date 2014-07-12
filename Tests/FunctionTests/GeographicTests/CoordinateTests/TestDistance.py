from nose.tools import *

from Core.Functions.Geographic.Coordinate import Distance

class Test_DistanceCalculaton:

	def Test_One(self):
		lat1 = 1
		long1 = 2
		lat2 = 3
		long2 = 4

		expected = 314.40295102361557
		actual = Distance.Distance_LatLongs(lat1, long1, lat2, long2)

		assert_equals(expected, actual)
