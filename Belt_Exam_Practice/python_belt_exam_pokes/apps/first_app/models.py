from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
import re,bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def currentUser(self, request):
        id=request.session['user_id']

        return User.objects.get(id=id)

    def validateUser(self,form_data):
        errors=[]
        if len(form_data['first_name'])==0:
            errors.append('First Name is Required.')
        if len(form_data['last_name'])==0:
            errors.append('last_name is Required.')
        if len(form_data['email'])==0:
            errors.append('Email is Required.')
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append('Please enter a valid email!')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')
        if form_data['password'] != form_data['password_confirmation']:
            errors.append('Password Confirmation must match Password.')

        return errors

    def validateLogin(self,form_data):
        errors=[]

        if len(form_data['email'])==0:
            errors.append('Email is Required.')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')

        return errors

    def createUser(self,form_data):
        password=str(form_data['password'])
        hashed_pw=bcrypt.hashpw(password, bcrypt.gensalt())

        user=User.objects.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            password=hashed_pw,
        )

        return user

class PokeManager(models.Manager):
    def createPoke(sel,poker,pokee):
        poke=Poke.objects.create(
            poker=poker,
            pokee=pokee,
        )

        return poke



class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    friends=models.ManyToManyField('self',related_name='like_by')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Poke(models.Model):
    poker=models.ForeignKey(User, related_name='poked')
    pokee=models.ForeignKey(User, related_name='poked_by')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=PokeManager()
