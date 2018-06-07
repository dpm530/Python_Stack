from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):

    def currentUser(self, request):
        id=request.session['user_id']

        return User.objects.get(id=id)

    def validateUser(self,form_data):
        errors=[]
        if len(form_data['full_name'])==0:
            errors.append('First Name is Required.')
        if len(form_data['alias'])==0:
            errors.append('Alias is Required.')
        if len(form_data['email'])==0:
            errors.append('Email is Required.')
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
            full_name=form_data['full_name'],
            alias=form_data['alias'],
            email=form_data['email'],
            password=hashed_pw,
        )

        return user

class BookManager(models.Manager):

    def bookValidation(self,form_data):
        errors=[]
        if len(form_data['title'])==0:
            errors.append('Title is Required.')
        if len(form_data['author'])==0:
            errors.append('Author is Required.')

        return errors


    def createBook(self,form_data,user):
        book=Book.objects.create(
            title = form_data['title'],
            author = form_data['author'],
            user = user,
        )
        return book

class ReviewManager(models.Manager):

    def createReview(self,form_data,book,user):
        review=Review.objects.create(
            content=form_data['content'],
            rating=form_data['rating'],
            book=book,
            user=user,
        )

        return review


class User(models.Model):
    full_name=models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    def __str__(self):
        return self.full_name

class Book(models.Model):
    title=models.TextField(max_length=255)
    author=models.TextField(max_length=255)
    user=models.ForeignKey(User,related_name='books')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BookManager()
    def __str__(self):
        return self.title

class Review(models.Model):
    content=models.TextField()
    rating=models.CharField(max_length=255)
    user=models.ForeignKey(User,related_name='reviews')
    book=models.ForeignKey(Book,related_name='reviews')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ReviewManager()
    def __str__(self):
        return self.content
