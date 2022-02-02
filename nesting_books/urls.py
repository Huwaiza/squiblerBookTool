from django.urls import path, include
from nesting_books.view import book
from rest_framework.routers import DefaultRouter

from nesting_books.view.book import BookModelViewset

router = DefaultRouter()

router.register('', BookModelViewset, basename='bookModelViewset')

urlpatterns = [
    path('book/', include(router.urls), name="book"),
    # path('create_section/', book),
]
