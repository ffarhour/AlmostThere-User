/*
	Interpolation.cpp

	Spider rajshorya@gmail.com
	*/

#include "stdafx.h"

#define INTERPOLATION_INTERPOLATION_MODULE
#include "Interpolation.h"

// #include <Cartesian.h>

PyObject * Interpolate_Linear(PyObject * self, PyObject  * args){
	double x0;
	double y0;

	double x1;
	double y1;

	double x;

	if (!PyArg_ParseTuple(args, "ddddd", &x0, &y0, &x1, &y1, &x)){
		return NULL;
	}

	double y = Linear_Interpolate(x0, y0, x1, y1, x);

	return PyFloat_FromDouble(y);
}

double Linear_Interpolate(double x0, double y0, double x1, double y1, double x){
	double y = y0 + (y1 - y0) * ((x - x0) / (x1 - x0));

	return y;
}