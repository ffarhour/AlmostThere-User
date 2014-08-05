from django.shortcuts import render
from django.http import HttpResponse

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

def btnClick(request):
	"""
	Ajax call
	"""
	context = []
	return "Welcome"
