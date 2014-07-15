import unittest

from Core.Functions.Math.Interpolation import Interpolate_Linear, Interpolate_Linear_3Points

class Test_Interpolation_Linear(unittest.TestCase):
	"""
	Tests linear interpolation
	"""
	def test_Linear_Interpolate_A(self):
		x0 = 1
		y0 = 1

		x1 = 3
		y1 = 3

		x = 2

		expected = 2
		actual = Interpolate_Linear(x0, y0, x1, y1, x)

		self.assertEqual(actual, expected)

class Test_Interpolation_Linear_3Points(unittest.TestCase):

	def test_Linear_Interpolate_3Points_A(self):
		x0 = 0
		y0 = 0
		z0 = 0

		x1 = 2
		y1 = 2
		z1 = 2

		distance = 1

		expected = (1, 1, 1)

		actual = Interpolate_Linear_3Points(x0, y0, z0, x1, y1, z1, distance)

		self.assertEqual(actual[0], expected[0])
		self.assertEqual(actual[1], expected[1])
		self.assertEqual(actual[2], expected[2])

if __name__ == '__main__':
	unittest.main()
