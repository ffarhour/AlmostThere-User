
# If set to true, then the native code in _Predictor is loaded
Native = False

from Core.Types import Point
from Core.Functions.Geographic.Coordinate import Distance_LatLongs

class Predictor:
	"""
	The python code for the Predictor
	"""

	def __init__(self):
		# The path that will be followed
		self.path = None

		# The destinaition that we aim to reach
		self.destination = None
		
		# THe current position, updated once we recieve data or interpolate
		self.currentPosition = None
		# List of all of the previous positions, updated whenever we add a new point	
		self.previousPositions = []

		# The predicted arrival time
		self.prediction = None

	def SetCurrentPosition(self, point):
		"""
		Sets the current position
		"""
		# So that we can correctly determine the position on a path
		self.previousPositions.append(self.currentPosition)

		self.currentPosition = point

		# self.Calculate()

	def SetDestination(self, point):
		"""
		Sets the destination - allowing us to make a prediction on the arrival time to the destination
		"""
		if type(point) != Point:
			raise TypeError("Incorrect Type")

		self.destination = point

	def SetPath(self, path):
		"""
		Sets the path to follow. If not set, then assumes straight distance
		"""

		for point in path:
			# Check if correct type
			if type(point) != Point:
				raise TypeError("Not of type Core.Types.Point")

		self.path = path

		
	def Calculate(self):
		"""
		Calculates the time needed to go along the path
		"""
		if self.destination == None:
			raise ValueError("Destination not set")

		if self.path == None:
			# If not path set, then assumes straight line, taking first point as the current position and the final point as destination
			self.path = []
			self.path.append(self.currentPosition)
			self.path.append(self.destination)

		prediction = self.Modifier_Base()

		self.prediction = prediction

		return prediction


	def Modifier_Base(self, average_speed, path = None, destination = None, currentPosition = None):
		"""
		The base modifier. This calculates the time based on distance and speed.

		Should be able to calculate the values based on data from within the class.

		However, there are optional parameters made available if this method is called outside of the Predictor class - such as from a unit test
		

		Params
		average_speed - The average speed of the object.
		path - The path to folllow
		destination - The destination point
		currentPosition - The current position, so that the distance may correctly be calculated

		Returns
		The expected time that the bus should take, in hours (as the great-circle formula is calculating the distance in km).
		"""

		if path == None:
			path = self.path

		if destination == None:
			destination = self.destination

		if currentPosition == None:
			currentPosition = self.currentPosition

		distance = 0

		# First we calculate the distance to travel
		for x in range(len(path)):
			# A for loop that loops through all of the points in the path
			if x == 0:
				# We are going to calculate the distance between the point and the one before, rather than this point and the one after
				continue

			# Calculate the great circle distance between points in the path
			distance += Distance_LatLongs(path[x].Latitude, path[x].Longitude, path[x-1].Latitude, path[x-1].Longitude)

		timeTaken = distance / average_speed
		
		# returns the time 
		return timeTaken



	def Modifier_API(self):
		"""
		Modifier that modifies the arrival time based on API data
		"""
		pass

	def Modifier_History(self):
		"""
		Modifies the data based on previous history of the bus
		"""
		pass

	def MOdifier_Traffic(self):
		pass

	def Modifier_UserGPS(self):
		"""
		Modifies the data based on data from user GPS positions
		"""
