from django.db import models
from django.urls import reverse


class Studio(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название студии')
    slug = models.SlugField(verbose_name='URL', max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studios', kwargs={'studio_url': self.slug})

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'


class GameGenre(models.Model):
    name = models.CharField(max_length=250, verbose_name='Жанр игры')
    slug = models.SlugField(verbose_name='URL', max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genres', kwargs={'genre_url': self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Platform(models.Model):
    name = models.CharField(max_length=250, verbose_name='Платформа')
    slug = models.SlugField(verbose_name='URL', max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('platforms', kwargs={'platform_url': self.slug})

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'


class Game(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название игры')
    date = models.DateField(verbose_name='Дата выхода игры')
    slug = models.SlugField(verbose_name='URL', max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(verbose_name='Описание игры')
    poster = models.ImageField(verbose_name='Постер игры', upload_to='games/')
    raiting = models.FloatField(verbose_name='Рейтинг Metacritic', null=True, blank=True)
    studio = models.ForeignKey(Studio, verbose_name='Студия игры', null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(GameGenre, verbose_name='Жанр игры', null=True, blank=True, on_delete=models.SET_NULL)
    platform = models.ManyToManyField(Platform, verbose_name='Платформа игры', related_name='game_platform')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def get_absolute_url(self):
        return reverse('games', kwargs={'game_url': self.slug})
