# Generated by Django 5.1.3 on 2024-12-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_remove_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('horror', 'Ужасы'), ('comedy', 'Комедия'), ('thriller', 'Триллер'), ('drama', 'Драма'), ('fantasy', 'Фантастика')], max_length=100, verbose_name='Жанр'),
        ),
    ]
