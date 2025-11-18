from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def ping_check(request):
    return Response({"status": "ok"})

# ModelViewSet автоматически создаёт стандартные 
# CRUD-операции для модели.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
