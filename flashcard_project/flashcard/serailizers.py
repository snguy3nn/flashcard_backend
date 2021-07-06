from rest_framework import serializers
from .models import Flashcard
from. models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'collection', 'subject', 'question', 'answer']


