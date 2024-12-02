from django import forms
from apps.movies.models import Movie, MovieRating

class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'cover', 'genre', 'release_year', 'video'] 

class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'cover', 'genre', 'release_year', 'video']  

class MovieRatingForm(forms.ModelForm):
    class Meta:
        model = MovieRating
        fields = ['score']