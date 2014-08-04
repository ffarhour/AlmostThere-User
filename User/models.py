from django.db import models
from datetime import datetime



class User(models.Model):
	"""
	The user
	"""
	DeviceID = models.IntegerField(default = -1)

class Bus(models.Model):
	"""
	The bus
	"""
	Bus_ID = models.CharField(max_length = 25)


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
	
	Route_ID = models.CharField(default = -1, max_length = 20)



class Shape_Points(models.Model):
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

	Stop_ID = models.CharField(max_length=15, default = -1)
