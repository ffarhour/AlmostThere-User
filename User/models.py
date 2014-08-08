from django.db import models
from datetime import datetime



class User(models.Model):
	"""
	The user
	"""
	DeviceID = models.IntegerField(default = -1, unique = True)

class Bus(models.Model):
	"""
	The bus
	"""
	Bus_ID = models.CharField(max_length = 25, unique = True)


class Position(models.Model):
	"""
	A record of the positions
	"""

	Latitude = models.FloatField(default = None)
	Longitude = models.FloatField(default = None)

	DateTime = models.DateTimeField(default = datetime.now())

class  Bus_Position(Position):
	"""
	A bus position
	"""
	bus = models.ForeignKey(Bus)

class User_Position(Position):
	"""
	A device position
	"""
	user = models.ForeignKey(User)



class Route(models.Model):
	"""
	A route
	"""
	
	Route_ID = models.CharField(default = -1, max_length = 20, unique = True)
	short_name = models.CharField(default = None, max_length = 10)


class Trip(models.Model):
	"""
	A trip
	"""

	TripID = models.CharField(max_length = 25, default = -1, unique = True)

	route = models.ForeignKey(Route)
	
	direction = models.IntegerField(default = -1)



class Shape_Point(models.Model):
	"""
	Different points on shapes, identified by shape id
	"""

	Latitude = models.FloatField(default = None)
	Longitude = models.FloatField(default = None)

	Shape_ID = models.CharField(max_length = 10, default = -1)

	route = models.ForeignKey(Route)


class Stop(models.Model):
	"""
	A stop
	"""

	Latitude = models.FloatField(default = None)
	Longitude = models.FloatField(default = None)

	Stop_ID = models.CharField(max_length=15, default = -1, unique = True)

class Stop_Time(models.Model):
	"""
	A stop time
	"""

	stop = models.ForeignKey(Stop)
	trip = models.ForeignKey(Trip)

	time = models.TimeField(default = datetime.now())

