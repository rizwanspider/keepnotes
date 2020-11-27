from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView
from rest_framework.views import APIView
from notesapp.models import ModelNote
from notesapp.api.serializers import SerializerNote

# Create your views here.
class ViewListNotes(APIView):
    """
    List all notes, or create a new note.
    """
    def get(self, request, format=None):
        notes = ModelNote.objects.all()
        serializer = ModelNoteSerializer(notes, many=True)
        return Response(serializer.data)