from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.views.decorators.csrf import csrf_protect



# Create your views here.
@csrf_protect
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

@csrf_protect
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
   