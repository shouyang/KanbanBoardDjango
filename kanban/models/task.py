import datetime
import uuid

from django.urls import reverse
from django.db import models


class Task(models.Model):
    class Meta:
        ordering = ['-date_modified']

    STATUS_CHOICES = {
        ('TODO', 'To Do'),
        ('PROG', 'In Progress'),
        ('TEST', 'In Testing'),
        ('DONE', 'Done'),
    }

    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    priority = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='TODO')

    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_modified = models.DateTimeField(default=datetime.datetime.now())
    author = models.CharField(max_length=200, default='No Author')

    def __str__(self):
        return '{title}'.format(title=self.title)

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.uuid})