from django.db import models

""" This is the book model which can have multiple sections"""
class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default=None)
    description = models.CharField(max_length=500, null=True, blank=True, default=None)

    def __str__(self):
        return self.title

""" Self referencing foreign key to use nested or recursive relationships"""
class BookSection(models.Model):
    section_title = models.CharField(max_length=200, null=True, blank=True, default=None)
    section_description = models.CharField(max_length=500, null=True, blank=True, default=None)
    parent_section = models.ForeignKey('nesting_books.BookSection', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="book_section", on_delete=models.CASCADE)

    def __str__(self):
        return self.section_title
