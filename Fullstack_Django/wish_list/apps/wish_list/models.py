from __future__ import unicode_literals
from django.db import models
import re,bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def currentUser(self,request):
        id=request.session['user_id']

        return User.objects.get(id=id)

    def validateUser(self,form_data):
        errors=[]

        if len(form_data['name'])==0:
            errors.append('Name cannot be empty.')
        if len(form_data['username'])==0:
            errors.append('Username cannot be empty.')
        if not EMAIL_REGEX.match(form_data['username']):
            errors.append('Please enter a valid username')
        if len(form_data['password'])==0:
            errors.append('Password cannot be empty.')
        if form_data['password'] != form_data['password_confirmation']:
            errors.append('Password and Password Confirmation must match!')

        return errors

    def validateLogin(self,form_data):
        errors=[]

        if len(form_data['username'])==0:
            errors.append('Username cannot be empty.')
        if len(form_data['password'])==0:
            errors.append('Password cannot be empty.')

        return errors


    def createUser(self, form_data):
        password=str(form_data['password'])
        hashed_pw=bcrypt.hashpw(password, bcrypt.gensalt())

        user=User.objects.create(
            name=form_data['name'],
            username=form_data['username'],
            password=hashed_pw,
        )

        return user

class WishListManager(models.Manager):

    def validateItem(self,form_data):
        errors=[]

        if len(form_data['addItem'])==0:
            errors.append('Item field cannot be empty.')

        return errors

    def createListItem(self,form_data,user):
        items=WishList.objects.create(
            item=form_data['addItem'],
            user=user,
        )

        return items



class User(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class WishList(models.Model):
    item=models.CharField(max_length=255)
    user=models.ForeignKey(User,related_name='list_items')
    users=models.ManyToManyField(User,related_name='other_wish_lists')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=WishListManager()
