from django.test import TestCase
from .models import ModelNote
from django.test import Client
import datetime

# Create your tests here.
class TestNotesAPI(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.note = ModelNote.objects.create(
            title='First Task', 
            content='Go and get the milk', 
            author='Riz Ahmed', 
            created=datetime.datetime.now(), 
            updated=datetime.datetime.now(), 
            published=datetime.datetime.now(),
        )
    
    def test_get_all_notes(self):
        # Issue a GET request.
        response = self.client.get('/api/notes/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
