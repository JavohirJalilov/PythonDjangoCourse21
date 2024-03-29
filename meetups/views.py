from django.shortcuts import render
from django.http import HttpResponse
from .models import Metup
# Create your views here.

def index(request):
	meetups = Metup.objects.all()
	return render(request, 'meetups/index.html',{
		'show_meetups':True,
		'meetups':meetups
	})

def meetups_details(request,meetup_slug):
	try:
		selected_meetup = Metup.objects.get(slug=meetup_slug)
		return render(request,'meetups/meetup-details.html',{
			'meetup_title':selected_meetup.title,
			"meetup_found":True,
			'meetup_description':selected_meetup.description
		})
	except Exception as exc:
		return render(request, 'meetups/meetup-details.html', {
			"meetup_found":False
		})
