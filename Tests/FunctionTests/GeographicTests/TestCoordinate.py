"""
Tests the Functions.Geographic.Coordinate module
"""

from nose.tools import *
import unittest

from Core.Functions.Geographic.Coordinate import Angle_LatLongs_And_Vertical

class Test_Angle_LatLongs_And_Vertical(unittest.TestCase):
	"""
	Tests the Angle_LatLongs_And_Vertical
	"""

	def Test_180Angle(self):

		lat1 = 1
		long1 = 1

		lat2 = 0
		long2 = 1

		expected = 180

		actual = Angle_LatLongs_And_Vertical(lat1, long1, lat2, long2)

		self.assertEqual(actual, expected)

	def Test_270Angle(self):

		lat1 = 1
		long1 = 1

		lat2 = 1
		long2 = 0

		expected = 270

		actual = Angle_LatLongs_And_Vertical(lat1, long1, lat2, long2)

		self.assertEqual(actual, expected)

	def Test_90Angle(self):

		lat1 = 1
		long1 = 1

		lat2 = 1
		long2 = 2

		expected = 90

		actual = Angle_LatLongs_And_Vertical(lat1, long1, lat2, long2)

		self.assertEqual(actual, expected)
