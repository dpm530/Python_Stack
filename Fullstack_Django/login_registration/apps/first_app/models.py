from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def validate(self,form_data):
        errors=[]
        if len(form_data['first_name'])==0:
            errors.append('First Name is Required.')
        if len(form_data['last_name'])==0:
            errors.append('Last Name is Required.')
        if len(form_data['email'])==0:
            errors.append('Email is Required.')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')
        if form_data['password'] != form_data['password_confirmation']:
            errors.append('Password Confirmation must match Password.')
        return errors

    def validate_login(self,form_data):
        errors=[]
        if len(form_data['email'])==0:
            errors.append('Email is Required.')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')
        return errors


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output= ' id: {}, first_name: {}, last_name: {}, email: {}, password: {}'
        return srting_output.format(self.id,self.first_name,self.last_name,self.email, self.password)

    objects=UserManager()
