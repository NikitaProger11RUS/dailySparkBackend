from django.shortcuts import render

from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

# ModelViewSet автоматически создаёт стандартные 
# CRUD-операции для модели.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
