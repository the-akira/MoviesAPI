from django.contrib import admin
from .models import Movie, Director, Actor, Genre, Screenshot

classes = [Genre, Screenshot]

class MovieAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_per_page = 20

class ActorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_per_page = 20

class DirectorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)

for c in classes:
    admin.site.register(c)