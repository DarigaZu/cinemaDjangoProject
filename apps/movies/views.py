from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
import random
from django.shortcuts import get_object_or_404, redirect
from django.views import View, generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from django.db.models import Avg
from apps.movies.models import Movie, MovieRating
from apps.movies.forms import MovieCreateForm, MovieUpdateForm, MovieRatingForm

logger = logging.getLogger(__name__)

class RateMovieView(LoginRequiredMixin, View):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieRatingForm(request.POST)

        if form.is_valid():
            rating, created = MovieRating.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={'score': form.cleaned_data['score']}
            )
            return redirect('detail', pk=movie.pk)

        return render(request, 'movies/detail.html', {'movie': movie, 'rating_form': form})

class RandomMovieView(View):
    def get(self, request):
        movies = list(Movie.objects.all())
        if movies:
            random_movie = random.choice(movies)
            return redirect('detail', pk=random_movie.pk)
        else:
            return redirect('index')

class MovieListView(generic.ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class MovieCreateView(generic.CreateView):
    model = Movie
    form_class = MovieCreateForm
    template_name = 'movies/create.html'
    success_url = reverse_lazy('index')

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating_form'] = MovieRatingForm()

        average_rating = self.object.ratings.aggregate(Avg('score'))['score__avg']
        context['average_rating'] = average_rating if average_rating is not None else "Нет оценок"

        if self.request.user.is_authenticated:
            user_rating = self.object.ratings.filter(user=self.request.user).first()
            context['user_rating'] = user_rating
        else:
            context['user_rating'] = None 

        return context

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class MovieUpdateView(generic.UpdateView):
    model = Movie
    form_class = MovieUpdateForm
    template_name = 'movies/update.html'
    success_url = reverse_lazy('index')

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class MovieDeleteView(generic.DeleteView):
    model = Movie
    template_name = 'movies/delete.html'
    success_url = reverse_lazy('index')
