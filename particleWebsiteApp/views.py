from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Particle
# Create your views here.
def index( request ):
	particles = Particle.objects
	return render( request, 'particleWebsiteApp/index.html', { 'all_particles': particles } )

def detail( request, particle_id ):
	particle_detail = get_object_or_404( Particle, pk = particle_id ) 
	return render( request, 'particleWebsiteApp/detail.html', { 'particle': particle_detail } )

def summary( request ):
	return render( request, 'particleWebsiteApp/summary.html')

def references( request ):
	return render( request, 'particleWebsiteApp/references.html')