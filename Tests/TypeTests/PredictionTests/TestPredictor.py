import unittest

from Core.Types import Point
from Core.Functions.Geographic.Coordinate import Distance_LatLongs

from Core.Types.Prediction import Predictor

class Test_Predictor_Setters(unittest.TestCase):
	"""
	Tests the setters in Core.Types.Prediction.Predictor
	"""

	def setUp(self):
		self.predictor = Predictor()
		self.point = Point()

	def test_SetCurrentPosition(self):
		self.predictor.SetCurrentPosition(self.point)

		self.assertEqual(self.predictor.currentPosition, self.point)

	def test_SetCurrentPosition_UpdatePrevopisPositions(self):
		self.predictor.SetCurrentPosition(self.point)
		
		point = Point(Latitude = 10, Longitude = 10)
		self.predictor.SetCurrentPosition(point)

		self.assertEqual(self.predictor.previousPositions[len(self.predictor.previousPositions) - 1], self.point)

		self.predictor.SetCurrentPosition(Point(Latitude = 20, Longitude = 20))
		
		self.assertEqual(self.predictor.previousPositions[len(self.predictor.previousPositions) - 1], point)


	def test_SetDestination(self):
		self.predictor.SetDestination(self.point)

		self.assertEqual(self.predictor.destination, self.point)

	def test_SetPath(self):
		points = []
		
		for x in range(10):
			points.append(Point(Latitude = x, Longitude = x))

		self.predictor.SetPath(points)

		self.assertEqual(self.predictor.path, points)

class Test_Predictor_Calculate(unittest.TestCase):
	"""
	Tests the calculate function
	"""
	def test_A(self):
		pass


class Test_Predictor_Base_Modifier(unittest.TestCase):
	"""
	Tests the Modifier_Base function
	"""

	def setUp(self):
		self.predictor = Predictor()
	
	def test_TwoPoint_CurrentHalfway(self):
		"""
		Tests the time calculation between two points, with the object halfway in between
		"""
		speed = 10

		pointA = Point(Latitude = 0, Longitude = 0)
		pointB = Point(Latitude = 10, Longitude = 10)

		distance = Distance_LatLongs(pointA.Latitude, pointA.Longitude, pointB.Latitude, pointB.Longitude)
		# As the bus is halfwway betwween the path
		distance = distance / 2;
		expected = distance / speed;

		self.predictor.SetDestination(pointB)

		path = []
		path.append(pointA)
		path.append(pointB)

		self.predictor.SetPath(path)

		# MidPoint
		self.predictor.SetCurrentPosition(Point(Latitude = 5, Longitude = 5))

		actual = self.predictor.Modifier_Base(average_speed = speed)

		self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main()
