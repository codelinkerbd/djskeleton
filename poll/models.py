import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True, verbose_name=_("Date Published"))

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_absolute_url(self):
        return reverse('poll:poll_details', kwargs={"pk": self.id})

    def __str__(self):
        return self.question_text




class Choice(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    @property
    def get_author(self):
        pass
    

