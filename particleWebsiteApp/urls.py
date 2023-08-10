from django.urls import path
from .import views

urlpatterns = [
	path( '', views.index, name = "index" ),
	path( '<int:particle_id>', views.detail, name = "detail" ),
	path( 'summary', views.summary, name = "summary" ),
	path( 'references', views.references, name = "references" ),
]