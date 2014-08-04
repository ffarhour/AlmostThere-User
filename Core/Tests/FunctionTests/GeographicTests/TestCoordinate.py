import unittest

"""
Tests the Functions.Geographic.Coordinate module
"""

from Core.Functions.Geographic.Coordinate import Angle_LatLongs_And_Vertical, Distance_LatLongs, ToGeo, ToCartesian

class Test_Angle_LatLongs_And_Vertical(unittest.TestCase):
	"""
	Tests the Angle_LatLongs_And_Vertical
	"""

	def test_180Angle(self):

		lat1 = 1
		long1 = 1

		lat2 = 0
		long2 = 1

		expected = 180

		actual = Angle_LatLongs_And_Vertical(lat1, long1, lat2, long2)

		self.assertEqual(actual, expected)

	def test_270Angle(self):

		lat1 = 1
		long1 = 1

		lat2 = 1
		long2 = 0

		expected = 270

		actual = Angle_LatLongs_And_Vertical(lat1, long1, lat2, long2)

		self.assertEqual(actual, expected)

	def test_90Angle(self):

		lat1 = 1
		long1 = 1

		lat2 = 1
		long2 = 2

		expected = 90

		actual = Angle_LatLongs_And_Vertical(lat1, long1, lat2, long2)

		self.assertEqual(actual, expected)

class Test_Distance_LatLongs(unittest.TestCase):

	def test_Basic_Small(self):

		expected = 157.24938127194397
		actual = Distance_LatLongs(0, 0, 1, 1)

		self.assertEqual(actual, expected)

	def test_Basic_Large(self):

		expected = 9724.91158548168
		actual = Distance_LatLongs(1, 1, 100, 100)

		self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
