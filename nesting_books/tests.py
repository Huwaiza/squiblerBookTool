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


class AssignParentSectionTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        book = Book.objects.create(title="Introduction to python unit testing")
        p_section = BookSection.create_section(title="Unit Test case", book=book,
                                               description="This is how unit test works")
        c_section = BookSection.create_section(title="API Test case", book=book,
                                               description="This is how API test works")

        self.assign_section_url = reverse('nesting_books:assign_parent_section')
        self.assign_req_data = {'assign_to_section_id': p_section.id, 'section_id': c_section.id}

    def test_assign_parent_section(self):
        self.client = APIClient()
        assign_section = self.client.post(self.assign_section_url, data=self.assign_req_data)
        self.assertJSONEqual(str(assign_section.content, encoding='utf8'),
                             {'success': True, 'message': "Book Section is assigned successfully!", "status_code": 200})


class DeleteSectionTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        book = Book.objects.create(title="Introduction to python unit testing")
        section = BookSection.create_section(title="Unit Test case", book=book,
                                             description="This is how unit test works")

        self.del_section_url = reverse('nesting_books:delete_section')
        self.del_sec_data = {'section_id': section.id}

    def test_delete_section(self):
        self.client = APIClient()
        del_section_resp = self.client.post(self.del_section_url, data=self.del_sec_data)
        self.assertJSONEqual(str(del_section_resp.content, encoding='utf8'),
                             {'success': True, 'message': "Book Section deleted successfully!", "status_code": 200})


class FetchAllBookSectionsTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        book = Book.objects.create(title="Introduction to python unit testing")
        BookSection.create_section(title="Unit Test case", book=book,
                                   description="This is how unit test works")

        self.fetch_section_url = reverse('nesting_books:fetch_all_sections')

    def test_fetch_all_section(self):
        self.client = APIClient()
        fetch_section_resp = self.client.get(self.fetch_section_url)
        assert fetch_section_resp.status_code == 200


class CreateSectionTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        book = Book.objects.create(title="Introduction to python unit testing")
        self.create_section_url = reverse('nesting_books:create_section')
        self.create_sec_data = {
            'section_title': 'This is test case section',
            'section_description': 'Some section description',
            'book': book.id,
        }

    def test_create_section(self):
        self.client = APIClient()
        cr_section_resp = self.client.post(self.create_section_url, data=self.create_sec_data)
        assert cr_section_resp.status_code == 200
