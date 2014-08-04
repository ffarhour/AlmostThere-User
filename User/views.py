from django.shortcuts import render

# Create your views here.

def index(request):
	"""
	The index page - the main website
	"""
	context = []
	return render(request, 'index.html', context)
