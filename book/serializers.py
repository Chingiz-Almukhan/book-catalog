from django.db.models import Avg
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from book.models import Genre, Author, Book, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    average_rating: SerializerMethodField = serializers.SerializerMethodField()

    def get_average_rating(self, book: object) -> object:
        avg_rating: object = book.review_set.aggregate(Avg('rating'))['rating__avg']
        return avg_rating if avg_rating is not None else 0

    class Meta:
        model = Book
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book', 'rating', 'text']
