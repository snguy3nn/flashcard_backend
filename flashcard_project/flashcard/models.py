from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=50)


class Flashcard(models.Model):
    subject = models.CharField(max_length=50)
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
