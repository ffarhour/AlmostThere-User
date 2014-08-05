#!env/Scripts/python

import os
# from datetime import time
import time

BASE_DIR = os.path.dirname(__file__)

resource_dir = os.path.join(BASE_DIR, "resources", "raw")

def populate():
	routes_File = open(os.path.join(resource_dir, "routes.txt"))
	stops_file = open(os.path.join(resource_dir, "stops.txt"))
	shape_file = open(os.path.join(resource_dir, "shapes.txt"))
	stop_times_file = open(os.path.join(resource_dir, "stop_times.txt"))
	trips_file = open(os.path.join(resource_dir, "trips.txt"))

	routes = routes_File.read().split('\n')
	routes.pop(0)
	routes_File.close()

	stops = stops_file.read().split('\n')
	stops.pop(0)
	stops_file.close()

	shapes = shape_file.read().split('\n')
	shapes.pop(0)
	shape_file.close()

	stop_times = stop_times_file.read().split('\n')
	stop_times.pop(0)
	stop_times_file.close()

	trips = trips_file.read().split('\n')
	trips.pop(0)
	trips_file.close()

	print("Loaded resources from files into memory")

	
	route_list = []
	for route in routes:
		route_list.append(Route(Route_ID = route.split(',')[0]))

	Route.objects.bulk_create(route_list)
	print("Created " + str(len(route_list)) + " routes")

	trips_list = []
	for trip in trips:
		trip_data = trip.split(',')
		trips_list.append(
		Trip(
			TripID = trip_data[2],
			route = Route.objects.get(Route_ID = trip_data[0]),
			direction = trip_data[4]
			)
				)

	Trip.objects.bulk_create(trips_list)
	print("Created " + str(len(trips_list)) + " trips")

	shapes_list = []
	for shape in shapes:
		shape_data = shape.split(',')
		# print(shape_data[0])
		shapes_list.append(
		Shape_Point(
		Latitude = float(shape_data[1]) ,
		Longitude = float(shape_data[2]),
		Shape_ID = shape_data[0] ,
		route =  FindRoute(routes, shape_data[0])
				))

	Shape_Point.objects.bulk_create(shapes_list)
	print("Created " + str(len(shapes_list)) + " shape points")

	
	stops_list = []
	for stop in stops:
		stop_data = stop.split(',')
		stops_list.append(
		Stop(
		Latitude = float(stop_data[3]),
		Longitude = float(stop_data[4]),
		Stop_ID =  stop_data[0]
			)
				)

	Stop.objects.bulk_create(stops_list)
	print("Created " + str(len(stops_list)) + " stops")

	stop_time_calc(stop_times)

def stop_time_calc(stop_times):
	stop_times_list = []
	for stop_time in stop_times:
		stop_time_data = stop_time.split(",")
		stop_times_list.append(
		Stop_Time(
		stop = Stop.objects.get(Stop_ID = stop_time_data[3]),
		trip = Trip.objects.get(TripID = stop_time_data[0]),
		# time = time.strptime(stop_time_data[2],"%H:%M:%S")
		time = stop_time_data[2]
		)
				)

	Stop_Time.objects.bulk_create(stop_times_list)
	print("Created " + str(len(stop_times_list)) + " stop times")

	print("Finished data upload")


		


def FindRoute(routes, shape_id):
	for route in routes:
		if route.split(',')[0][-4:] == shape_id:
			return Route.objects.get(Route_ID = route.split(',')[0])





if __name__ == '__main__':
    print("Starting population script...")
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UserSite.settings')
    django.setup()
    from User.models import Route, Stop, Shape_Point, Trip, Stop_Time

    populate()
    
    # stop_times = open(os.path.join(BASE_DIR, "resources", "raw", "stop_times.txt")).read().split('n')
    # stop_times.pop(0)
    # stop_time_calc(stop_times)
