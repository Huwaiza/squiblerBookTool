from django.urls import path, include
from nesting_books.view import book
from rest_framework.routers import DefaultRouter

from nesting_books.view.book import BookModelViewset, CreateBookSection, BookSectionList, DeleteBookSection, \
    AssignToParentSection, UnassignBookSection

app_name = 'nesting_books'

router = DefaultRouter()

router.register('', BookModelViewset, basename='bookModelViewset')

urlpatterns = [
    path('book/', include(router.urls), name="book"),
    path('create_section/', CreateBookSection.as_view(), name="create_section"),
    path('fetch_all_sections/', BookSectionList.as_view(), name="fetch_all_sections"),
    path('delete_section/', DeleteBookSection.as_view(), name="delete_section"),
    path('assign_parent_section/', AssignToParentSection.as_view(), name="assign_parent_section"),
    path('unassign_parent_section/', UnassignBookSection.as_view(), name="unassign_parent_section"),
]
