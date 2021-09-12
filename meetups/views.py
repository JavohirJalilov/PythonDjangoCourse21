from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	meetups = [
		{'title':'A First Meetup'},
		{'title':'A Second Meetup'}
	]
	return render(request, 'meetups/index.html',{
		'show_meetups':True,
		'meetups':meetups
	})