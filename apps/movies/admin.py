from django.contrib import admin
from apps.movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    exclude = ('author',)  

    def save_model(self, request, obj, form, change):
        if not change: 
            obj.author = request.user 
        super().save_model(request, obj, form, change)

admin.site.register(Movie, MovieAdmin)