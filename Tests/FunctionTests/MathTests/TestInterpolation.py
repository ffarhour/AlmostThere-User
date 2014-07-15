import unittest

from Core.Functions.Math.Interpolation import Interpolate_Linear

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

if __name__ == '__main__':
	unittest.main()
