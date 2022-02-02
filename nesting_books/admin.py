from django.contrib import admin

from nesting_books.models import Book, BookSection

admin.site.register(Book)
admin.site.register(BookSection)
