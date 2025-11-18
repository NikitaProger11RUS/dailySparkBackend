from rest_framework import serializers
from .models.note import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note        # какие объекты обрабатывать
        fields = '__all__'  # какой сериализатор использовать