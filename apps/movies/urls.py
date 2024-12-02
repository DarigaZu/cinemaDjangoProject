from django.urls import path
from apps.movies import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'),
    path('create/', views.MovieCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.MovieUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='delete'),
    path('movies/random/', views.RandomMovieView.as_view(), name='random_movie'),
    path('movies/<int:pk>/rate/', views.RateMovieView.as_view(), name='rate_movie'),
]
