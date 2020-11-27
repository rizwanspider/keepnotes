from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from notesapp.models import ModelNote   
from django.utils import timezone
import json

class TestCaseAPIAccountCredits(APITestCase):
    urlpatterns = [
        path('api/', include('notesapp.api.urls')),
    ]

    def setUp(self):
        self.valid_payload = {
            'title': 'My First Note', 
            'content': 'Go and get the milk',
            'author': 'Rizwan Ahmed', 
            'published': timezone.now()
        }
        self.invalid_payload = {
            'title': 'My Invalid Note', 
            'content': 'Go to hell',
            'author': 'Sulakhan Singh', 
            'published': 'today'
        }
        self.first_note = ModelNote.objects.create(**self.valid_payload)

    def test_create_note(self):
        """
        Ensure we can create a new note object.
        """
        url = reverse('create')
        data = {
            'title': 'Weekend Plans', 
            'content': 'Will go for outting',
            'author': 'Sagar', 
            'published': timezone.now()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_all_notes(self):
        url = reverse('note-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_note_detail(self):
        kwargs = {'pk': self.first_note.pk}
        url = reverse('note-detail', kwargs=kwargs)
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'], 'Rizwan Ahmed')
    
    def test_get_invalid_note_detail(self):
        kwargs = {'pk': 30}
        url = reverse('note-detail', kwargs=kwargs)
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_update_single_note(self):
        kwargs = {'pk': self.first_note.pk}
        url = reverse('note-detail', kwargs=kwargs)
        data = json.dumps({'title': 'YES'})

        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    

    def test_delete_single_note(self):
        kwargs = {'pk': self.first_note.pk}
        url = reverse('note-detail', kwargs=kwargs)

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

