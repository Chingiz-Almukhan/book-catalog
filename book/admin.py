from django.contrib import admin

from book.models import Review, Author, Genre, Book

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Review)

