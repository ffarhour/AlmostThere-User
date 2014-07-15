/*
	Cartesian.cpp
	Allows for the conversion of latitude and longitude points into cartesian coordinates

	Spider rajshorya@gmail.com
	*/

#include "stdafx.h"

#define COORDINATE_CARTESIAN_MODULE
#include "Cartesian.h"

/*
	Using http://stackoverflow.com/questions/1185408/converting-from-longitude-latitude-to-cartesian-coordinates
	*/
PyObject * ToCartesian(PyObject * self, PyObject * args){
	double lat1;
	double long1;

	if (!PyArg_ParseTuple(args, "dd", &lat1, &long1)){
		return NULL;
	}

	double cartesian[3];
	_ToCartesian(lat1, long1, cartesian);

	return Py_BuildValue("ddd", cartesian[0], cartesian[1], cartesian[3]);
}

void _ToCartesian(double lat, double lon, double cartesian[3]){
	double const Radius = 6371;

	cartesian[0] = Radius * cos(lat) * cos(lon);
	cartesian[1] = Radius * cos(lat) * sin(lon);
	cartesian[2] = Radius * sin(lat);
}

// http://stackoverflow.com/questions/1185408/converting-from-longitude-latitude-to-cartesian-coordinates
PyObject * ToGeo(PyObject * self, PyObject * args){
	double x;
	double y;
	double z;

	if (!PyArg_ParseTuple(args, "ddd", &x, &y, &z)){
		return NULL;
	}

	double geo[2];

	_ToGeo(x, y, z, geo);

	return Py_BuildValue("dd", geo[1], geo[0]);
}

void _ToGeo(double x, double y, double z, double geo[2]){
	double const Radius = 6371;

	geo[1] = asin(z / Radius);
	geo[0] = atan2(y, x);
}