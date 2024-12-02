from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg

User = get_user_model()

class Movie(models.Model):
    cover = models.ImageField(upload_to='movies/img/', verbose_name='Обложка фильма', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    genre = models.CharField(max_length=100, verbose_name='Жанр')
    release_year = models.IntegerField(verbose_name='Год выпуска')
    video = models.FileField(upload_to='movies/videos/', verbose_name='Видео', blank=True, null=True) 
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        verbose_name='Автор'
    )

    def __str__(self):
        return self.cover, self.title
    
    def average_rating(self):
        return self.ratings.aggregate(Avg('score'))['score__avg'] or 0.0
    

class MovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.FloatField()

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title} - {self.score}"