from django.db import models

import datetime
import uuid

from .import Task


class TaskComment(models.Model):
    class Meta:
        ordering = ['-date_created']

    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()

    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_modified = models.DateTimeField(default=datetime.datetime.now())
    author = models.CharField(max_length=200, default='No Author')

    def __str__(self):
        return '{author} - {task}:{text}...'.format(author=self.author, task=self.task.title, text=self.text[:25])