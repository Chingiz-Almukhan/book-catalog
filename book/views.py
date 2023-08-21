from typing import Type, Any

from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book, Genre, Author, Review
from book.serializers import BookSerializer, GenreSerializer, AuthorSerializer, ReviewSerializer


def index(request):
    return render(request, "index.html")


class BookListView(generics.ListCreateAPIView):
    queryset: QuerySet[Book] = Book.objects.all()
    serializer_class: Type[BookSerializer] = BookSerializer


    def get_queryset(self):
        qs: QuerySet | Any = super().get_queryset()

        genre: object = self.request.query_params.get('genre', None)
        if genre:
            try:
                found_genre: Genre = Genre.objects.get(name__icontains=genre)
            except Genre.DoesNotExist:
                return []
            if found_genre.id:
                qs = qs.filter(genre_id=found_genre.id)

        author: object = self.request.query_params.get('author', None)
        if author:
            try:
                found_author: Author = Author.objects.get(name__icontains=author)
            except Author.DoesNotExist:
                return []
            if found_author.id:
                qs = qs.filter(author_id=found_author.id)

        min_date: object = self.request.query_params.get('date-min', None)
        if min_date:
            qs = qs.filter(publication_date__gte=min_date)

        max_date: object = self.request.query_params.get('date-max', None)
        if max_date:
            qs = qs.filter(publication_date__lte=max_date)

        return qs


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset: QuerySet[Book] = Book.objects.all()
    serializer_class: Type[BookSerializer] = BookSerializer


class BookFavoriteView(APIView):
    permission_classes: list[Type[IsAuthenticated]] = [IsAuthenticated]

    def post(self, request, pk):
        book: Book = get_object_or_404(Book, pk=pk)

        if book.user_favorite.filter(pk=request.user.pk).exists():
            book.user_favorite.remove(request.user)
            result: str = 'deleted'
        else:
            book.user_favorite.add(request.user)
            result: str = 'added'

        return Response({'result': result}, status=status.HTTP_200_OK)


class GenreCreateView(generics.CreateAPIView):
    queryset: QuerySet[Genre] = Genre.objects.all()
    serializer_class: Type[GenreSerializer] = GenreSerializer


class GenreDetailView(generics.RetrieveAPIView):
    queryset: QuerySet[Genre] = Genre.objects.all()
    serializer_class: Type[GenreSerializer] = GenreSerializer


class AuthorCreateView(generics.CreateAPIView):
    queryset: QuerySet[Author] = Author.objects.all()
    serializer_class: Type[AuthorSerializer] = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    queryset: QuerySet[Author] = Author.objects.all()
    serializer_class: Type[AuthorSerializer] = AuthorSerializer


@api_view(['GET'])
def get_reviews(request, book_id):
    reviews: QuerySet[Review] = Review.objects.filter(book_id=book_id)
    serializer: ReviewSerializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    serializer: ReviewSerializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
