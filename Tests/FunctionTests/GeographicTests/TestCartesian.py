import unittest

from Core.Functions.Geographic.Coordinate import ToGeo, ToCartesian

class Test_ToCartesian(unittest.TestCase):
	"""
	Tests ToCartesian
	"""
	def test_AllZero(self):
		lat = 0
		lon = 0

		expectedx = 6371
		expectedy = 0
		expectedz = 0

		results = ToCartesian(lat, lon)

		actualx = results[0]
		actualy = results[1]
		actualz = results[2]

		self.assertEquals(actualx, expectedx)
		self.assertEquals(actualy, expectedy)
		self.assertEquals(actualz, expectedz)

class Test_ToGeo(unittest.TestCase):

	def test_GEO_A(self):
		"""
		with x = 6371
			y = 0
			z = 0
		"""
		x = 6371
		y = 0
		z = 0

		expectedLat = 0
		expectedLong = 0

		results = ToGeo(x, y, z)

		actuallat = results[1]
		actuallon = results[0]

		self.assertEqual(actuallat, expectedLat)
		self.assertEqual(actuallon, expectedLong)


if __name__ == '__main__':
	unittest.main()
