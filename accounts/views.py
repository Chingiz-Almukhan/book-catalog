from django.db.models import QuerySet
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import UserSerializer
from book.models import Book

from book.serializers import BookSerializer


@api_view(['POST'])
def register_user(request):
    serializer: UserSerializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_favorites(request):
    user: Account = Account.objects.get(id=request.user.id)
    favorite_books: QuerySet[Book] = user.favorite_books.all()
    serializer: BookSerializer = BookSerializer(favorite_books, many=True)
    return Response(serializer.data, status=200)
