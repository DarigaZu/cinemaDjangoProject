from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name='никнейм')
    avatar = models.ImageField(upload_to='users/avatar/', verbose_name='аватарка', blank=True, null=True)
    bio = models.TextField(verbose_name='био', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
