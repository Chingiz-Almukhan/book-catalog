from django.urls import path

from book import views
from book.views import BookDetailView, BookListView, GenreCreateView, AuthorCreateView, AuthorDetailView, \
    GenreDetailView, BookFavoriteView

urlpatterns = [
    path('', views.index, name='main'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('genre/create/', GenreCreateView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),

    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    path('add_to_favorite/<int:pk>/', BookFavoriteView.as_view(), name='add_to_favorite'),

    path('reviews/<int:book_id>/', views.get_reviews, name='get_reviews'),
    path('reviews/create/', views.create_review, name='create_review'),
]
