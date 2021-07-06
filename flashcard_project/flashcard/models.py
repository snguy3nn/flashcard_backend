from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Collection Name: {self.name}"


class Flashcard(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return f"Flashcard Subject: {self.subject}"

