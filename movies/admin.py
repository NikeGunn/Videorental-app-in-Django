from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('title', 'number_in_stock', 'daily_rate' )
    list_filter = ('date_created',)
    


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
