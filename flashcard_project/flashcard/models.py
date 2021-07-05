from django.db import models


class Flashcard(models.Model):
    subject = models.CharField(max_length=50)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
