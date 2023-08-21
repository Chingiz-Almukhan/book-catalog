from datetime import date

from django.db import models
from django.contrib.auth.models import User

from accounts.models import Account


class Genre(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, null=False, blank=False)


class Author(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, null=False, blank=False)


class Book(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)
    genre = models.ForeignKey(verbose_name='Жанр id', to=Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(verbose_name='Автор id', to=Author, on_delete=models.CASCADE)
    publication_date = models.DateField(verbose_name='Дата публикации', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=False, blank=False)


class Review(models.Model):
    book = models.ForeignKey(verbose_name='Книга id', to=Book, on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='Пользователь id', to=Account, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(verbose_name='Рейтинг', default=1, null=False, blank=False)
    text = models.TextField(verbose_name='Отзыв', null=False, blank=False)
