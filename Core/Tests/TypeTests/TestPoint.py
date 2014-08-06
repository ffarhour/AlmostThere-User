"""
Tests the Point module

.. moduleauthor: SbSpider rajshorya@gmail.com
"""

from datetime import datetime
from nose.tools import *

from Core.Types import Point

class Test_PointInitialization:
	"""
	Tests the initialization of points
	"""

	def Test_NoDataSpecified(self):
		"""
		Tests the initialization of the point when no data is specified
		"""
		point = Point()

		assert_equals(point.DeviceID, 0)
		assert_equals(point.Latitude, 0)
		assert_equals(point.Longitude, 0)
		assert_equals(point.DateTime, datetime.now())

	def Test_DateTimeSpecified(self):
		"""
		Tests if the datetime is specified
		"""

		time = datetime.now()

		point = Point(DateTime = time)

		assert_equals(point.DateTime, time)

	@raises(Exception)
	def Test_ExceptionThrownWhenWrongInput_DeviceID(self):
		"""
		Tests if an error is given if the DeviceID is not an integer
		"""
		point = Point(DeviceID = 'asd')

	@raises(Exception)
	def Test_ExceptionThrownWhenWrongInput_Latitude(self):
		"""
		TEsts if an error is given if the Latitude is not a float
		"""
		point = Point(Latitude = 'asd')

	@raises(Exception)
	def Test_ExceptionThrownWhenWrongInput_Longitude(self):
		"""
		Tests if an error is given if the Longitude is not a float
		"""
		point = Point(Longitude = 'asd')

	@raises(Exception)
	def Test_ExceptionThrownWhenWrongInput_DateTime(self):
		"""
		Tests if an error is given if the DateTime is not parseable
		"""

		point = Point(DateTime = 'asd')
