from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notesapp.models import ModelNote
from notesapp.api.serializers import SerializerNote
from rest_framework import generics
from django.http import Http404

# Create your views here.
class ViewAPIListNotes(APIView):
    """
    List all notes.
    """
    def get(self, request, format=None):
        notes = ModelNote.objects.all()
        serializer = SerializerNote(notes, many=True)
        return Response(serializer.data)
        # return Response(status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = SerializerNote(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewAPIDetailNote(APIView):
    """
    Retrieve, update or delete a note instance.
    """
    def get_object(self, pk):
        try:
            return ModelNote.objects.get(pk=pk)
        except ModelNote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = SerializerNote(note)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = SerializerNote(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
