import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField()
    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content

    def was_published_at(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)
