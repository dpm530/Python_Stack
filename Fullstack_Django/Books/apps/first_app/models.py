from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    description=models.TextField()
    in_print=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
