from rest_framework import serializers

from nesting_books.models import Book, BookSection


# serializer for book model
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# serializer for creating section of book
class CreateBookSectionSerializer(serializers.Serializer):
    section_title = serializers.CharField(required=True)
    section_description = serializers.CharField(required=False)
    parent_section = serializers.IntegerField(required=False)
    book = serializers.IntegerField(required=True)

    class Meta:
        fields = '__all__'


# serializer for book sections
class BookSectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSection
        fields = '__all__'


class DeleteBookSectionSerializer(serializers.Serializer):
    section_id = serializers.IntegerField(required=True)

    class Meta:
        fields = '__all__'


class AssignBookSectionSerializer(serializers.Serializer):
    section_id = serializers.IntegerField(required=True)
    assign_to_section_id = serializers.IntegerField(required=True)

    class Meta:
        fields = '__all__'


class UnassignBookSectionSerializer(serializers.Serializer):
    section_id = serializers.IntegerField(required=True)

    class Meta:
        fields = '__all__'
