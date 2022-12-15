from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie, Genre

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
      
# class GenreResource(ModelResource):
#     class Meta:
#         queryset = Genre.objects.all()
#         resource_name = 'genre'
      

