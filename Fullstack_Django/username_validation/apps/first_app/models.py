from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validation(self,username):
        if EMAIL_REGEX.match(username) and len(username)>8 and len(username)<26:
            return True
        else:
            return False


class User(models.Model):
    username=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
