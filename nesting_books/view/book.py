from rest_framework import viewsets, permissions
from nesting_books.models import Book
from nesting_books.serializers import BookModelSerializer


class BookModelViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    permission_classes = (permissions.AllowAny,)