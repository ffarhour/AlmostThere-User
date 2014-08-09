from django.shortcuts import render
from django.http import HttpResponse

from Core.Types.Prediction import Predictor
from Core.Types import Point

from User.models import Stop, Route, Shape_Point, Stop_Time

from datetime import timedelta, datetime
import math

# Create your views here.

def index(request):
	"""
	The index page - the main website
	"""
	context = []
	return render(request, 'index.html', context)
def AlmostThere(request):
	"""
	The AlmostThere page - the screen
	"""
	context = []
	return render(request, 'AlmostThere.html', context)

def ButtonOne(request):
	"""
	Ajax call
	"""
	context = []
	return HttpResponse("welcome")

def ButtonNavigation(request):
	"""
	Navigate to Navigation page
	"""
	context = []
	return render(request, "Navigation.html", context)

def ButtonNavTimer(request):
	"""
	For the Timer
	"""


	stopOne = Stop.objects.get(Stop_ID =  request.GET['firstStop'])
	# stopTwo = Stop.objects.get(Stop_ID =  request.GET['secondStop'])
	# route = Route.objects.get(Route_ID = request.GET['route'])

	# predictor = Predictor()

	#predictor.SetCurrentLocation(Point(stopOne.Latitude, stopOne.Longitude))
	# predictor.SetDestination(Point(stopTwo.Latitude, stopTwo.Longitude))

	# shape_info = Shape_Point.objects.filter(route = route)
	# points_list = []
	# for shape in shape_info:
	#	points_list.append(
	#			Point(
	#			Latitude = shape.Latitude,
	#			Longitude = shape.Longitude
	#				))

	trips = []

	for stop_time in Stop_Time.objects.filter(stop = stopOne):
		if stop_time.time < (datetime.now() + timedelta(minutes=1)).time():
			if stop_time.trip not in trips:
				trips.append(stop_time.trip)
			

	#predictor.SetDestination(points_list[len(points_list)-1])
	# predictor.SetPath(points_list)
	# predictor.SetCurrentPosition(points_list[0])
	# arrival_time = predictor.Calculate(30)
				
	route_list = []
	for trip in trips:
		if trip.route not in route_list:
			route_list.append(trip.route)

	context = {'route_list' : route_list,
			'stop' : request.GET['firstStop']
			}
	

	return render(request, "Timer.html", context)

def TimerData(request):
	"""
	For the TimerData
	"""
	predictor = Predictor()

	route = Route.objects.get(Route_ID = request.GET['route_id'])
	stopOne = Stop.objects.get(Stop_ID =  request.GET['stop'])
	


	shape_info = Shape_Point.objects.filter(route = route)
	
	points_list = []
	for shape in shape_info:
		points_list.append(
				Point(
					Latitude = shape.Latitude,
					Longitude = shape.Longitude
					))

	predictor.SetPath(points_list)
	predictor.SetCurrentPosition(points_list[0])
	predictor.SetDestination(Point(
		Latitude = stopOne.Latitude,
		Longitude = stopOne.Longitude))

	time_taken = predictor.Calculate(30)
    
	return HttpResponse("<div id='timer' class='timer'> Bus is arriving in " + str(math.floor(time_taken*60)) + " minutes & " + str(math.ceil((time_taken - (math.floor(time_taken*60))/60)*3600)) + " seconds")
