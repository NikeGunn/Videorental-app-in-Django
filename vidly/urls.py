from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource
from . import views

admin.site.site_title = "Admin Panel"
admin.site.site_header = "Project Admin Panel"


movie_resource = MovieResource()
# genre_resource = GenreResource()



urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls)),
    # path('api/', include(genre_resource.urls)),
]
