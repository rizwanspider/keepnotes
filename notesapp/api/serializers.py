from rest_framework import serializers
from notesapp.models import ModelNote

class SerializerNote(serializers.ModelSerializer):
    class Meta:
        model = ModelNote
        # fields = '__all__'
        fields = ('title', 'content', 'author',  'published')