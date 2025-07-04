from django.db import models

# Create your models here.
from django import forms
import datetime
from django.utils import timezone

from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)
    message = models.CharField( max_length=500)

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return str(self.id)
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        

