/*
Distance.cpp

Distance functions
*/

#include <math.h>

#ifdef _DEBUG
#define DEBUG_WAS_DEFINED
#undef _DEBUG
#endif

#include <Python.h>

#ifdef DEBUG_WAS_DEFINED
#define _DEBUG 1
#undef DEBUG_WAS_DEFINED
#endif

double Degree2Radian(double);

static PyObject * Calculate_Distance_Between_Latitude_And_Longitude(PyObject * self, PyObject * args){
	const int Earth_Radius = 6371;

	double lat1;
	double lat2;

	double long1;
	double long2;

	// Grabs the arguements, 4 doubles
	if (!PyArg_ParseTuple(args, "dddd", &lat1, &long1, &lat2, &long2)){
		return NULL;
	}

	double dLat = Degree2Radian(lat2 - lat1);
	double dLong = Degree2Radian(long2 - long1);

	lat1 = Degree2Radian(lat1);
	lat2 = Degree2Radian(lat2);

	double a = sin(dLat / 2) * sin(dLat / 2) + cos(lat1) * cos(lat2) * sin(dLong / 2) * sin(dLong / 2);
	double c = 2 * atan2(sqrt(a), sqrt(1 - a));
	double d = Earth_Radius * c;

	return PyFloat_FromDouble(d);
}

static PyMethodDef DistanceMethods[] = {
		{ "Distance_LatLongs", Calculate_Distance_Between_Latitude_And_Longitude, METH_VARARGS, "Returns the distance between two sets off latitude and longitude points. Parameters: Lat1, Long1, Lat2, Long2" },
		{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef DistanceModule = {
	PyModuleDef_HEAD_INIT,
	"Coordinate",
	NULL,
	-1,
	DistanceMethods
};

PyMODINIT_FUNC PyInit_Distance(void){
	return PyModule_Create(&DistanceModule);
}

// ===================================
// Helper functions (not exported)
// ===================================

double Degree2Radian(double degree){
	return degree * (3.1415926535897 / 180);
}