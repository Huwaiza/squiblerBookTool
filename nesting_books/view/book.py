from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response

from nesting_books.models import Book, BookSection
from nesting_books.serializers import BookModelSerializer, CreateBookSectionSerializer


class BookModelViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    permission_classes = (permissions.AllowAny,)


class CreateBookSection(generics.GenericAPIView):
    serializer_class = CreateBookSectionSerializer

    def post(self, request):
        serializer = CreateBookSectionSerializer(data=request.data)
        if serializer.is_valid():
            section_title = request.POST.get('section_title')
            section_description = request.POST.get('section_description')
            parent_section_id = request.POST.get('parent_section')
            book_id = request.POST.get('book')

            book = Book.objects.filter(id=book_id).first() if book_id else None
            parent_book_section = BookSection.objects.filter(
                id=parent_section_id).first() if parent_section_id else None

            if book:
                book_section = BookSection.create_section(title=section_title, book=book,
                                                          description=section_description,
                                                          parent_section=parent_book_section)
                if book_section:
                    return Response({
                        "success": True,
                        "message": "Book Section created successfully!",
                        "result": {
                            "section_id": book_section.id,
                            "section_title": book_section.section_title,
                            "section_description": book_section.section_description,
                            "book_id": book_section.book.id,
                            "parent_section_id": book_section.parent_section.id
                        },
                        "status_code": status.HTTP_201_CREATED,
                    })
                else:
                    return Response({
                        "success": False,
                        "message": "Could not create book section",
                        "status_code": status.HTTP_400_BAD_REQUEST,
                    })
            else:
                return Response({
                    "success": False,
                    "message": "Cannot find instance of book! Sorry",
                    "status_code": status.HTTP_400_BAD_REQUEST,
                })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
