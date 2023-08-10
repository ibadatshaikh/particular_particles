from django.db import models

# Create your models here.
class Particle( models.Model ):
	name = models.CharField( max_length = 20 )
	charge = models.CharField( max_length = 20 )
	fundamental = models.CharField( max_length = 200 )
	summary = models.CharField( max_length = 500 )
	short_summary = models.CharField( max_length = 200 )
	fun_fact = models.CharField( max_length = 200 )
	image = models.CharField( max_length = 200 )
	image_caption = models.CharField( max_length = 100 )
	image_source = models.CharField( max_length = 500 )
	def __str__( self ):
		return self.summary

	
