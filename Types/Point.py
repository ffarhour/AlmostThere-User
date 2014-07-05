"""

.. module: Point
.. moduleauthor: SbSpider rajshorya@gmail.com

This module contains the code for the operation of the Point class
"""

from datetime import datetime

class Point:
	"""
	The point class, a standard means by which to transmit Point data throughout our application
	"""

	def __init__(self, DeviceID = 0, Latitude = 0, Longitude = 0, DateTime = None):
		"""
		DeviceID - The deviceid that logged the point
		Latitude - The Latitude of the point inserted
		Longitude - The Longitude of the point inserted
		DateTime - The DateTime at which the point was inserted

		All of the parameters are optional, as in some cases it may make more sense to set them at a later time
		"""

		self.DeviceID = int(DeviceID)
		self.Latitude = float(Latitude)
		self.Longitude = float(Longitude)

		if DateTime == None:
			self.DateTime = datetime.now()
		else:
			if type(DateTime) == datetime:
				self.DateTime = DateTime
			else:
				raise ValueError("DateTime is not of type datetime or parseable")
