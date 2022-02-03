from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.test import APIClient

from nesting_books.models import Book, BookSection


class UnassignParentSectionTestCase(TransactionTestCase):
    reset_sequences = True

    """ In setup we will keep the data we want to use in our test cases, rest sequence is True when objects are created
     multiple times there DB indexing could be re initiated """

    def setUp(self):
        book = Book.objects.create(title="Introduction to python unit testing")
        p_section = BookSection.create_section(title="Unit Test case", book=book,
                                               description="This is how unit test works")
        c_section = BookSection.create_section(title="API Test case", book=book,
                                               description="This is how API test works", parent_section=p_section)

        self.unassign_section_url = reverse('nesting_books:unassign_parent_section')
        self.unassign_req_data = {'section_id': c_section.id}

    def test_unassign_parent_section(self):
        self.client = APIClient()
        unassign_section = self.client.post(self.unassign_section_url, data=self.unassign_req_data)
        self.assertJSONEqual(str(unassign_section.content, encoding='utf8'),
                             {'success': True, 'message': "Book Section unassigned successfully!", "status_code": 200})
