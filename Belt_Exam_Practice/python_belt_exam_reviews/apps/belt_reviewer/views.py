from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Count
import bcrypt
from .models import User,Book,Review

def flashErrors(request,errors):
    for error in errors:
        messages.error(request,error)

def index(request):
    return render(request,'belt_reviewer/index.html')

def homePage(request):
    current_user=User.objects.currentUser(request)
    books=Book.objects.all().order_by('-created_at')

    context={
        'user': current_user,
        'books':books,
    }

    return render(request,'belt_reviewer/homePage.html', context)

def register(request):
    if request.method=='POST':
        errors=User.objects.validateUser(request.POST)
        if not errors:
            print 'Create User'
            user=User.objects.createUser(request.POST)

            request.session['user_id']=user.id

            return redirect('/homePage')

        flashErrors(request,errors)
    return redirect('/')

def login(request):
    if request.method=='POST':
        errors=User.objects.validateLogin(request.POST)
        if not errors:
            user=User.objects.filter(email=request.POST['email']).first()

            if user:
                password=str(request.POST['password'])
                user_password=str(user.password)

                hashed_pw=bcrypt.hashpw(password,user_password)

                if hashed_pw==user_password:
                    request.session['user_id']=user.id

                    return redirect('/homePage')

            errors.append('Invalid account Information')
        flashErrors(request,errors)

    return redirect('/')

def createWindow(request):
    return render(request,'belt_reviewer/createWindow.html')

def createNewBook(request):
    if request.method=='POST':
        errors=Book.objects.bookValidation(request.POST)
        if not errors:
            current_user=User.objects.currentUser(request)
            book=Book.objects.createBook(request.POST, current_user)
            review = Review.objects.createReview(request.POST, book, current_user)

            route = "/newBook/{}".format(book.id)
            return redirect(route)

        flashErrors(request,errors)

    return redirect('/homePage')

def newBook(request,book_id):
    current_user=User.objects.currentUser(request)
    book=Book.objects.get(id=book_id)
    reviews=book.reviews.all()

    print reviews

    context={
        'user': current_user,
        'book':book,
        'reviews':reviews
    }


    return render(request,'belt_reviewer/newBook.html', context)

def deleteReview(request,review_id):
    if request.method=='POST':
        print review_id
        review=Review.objects.get(id=review_id)

        book_id=review.book.id

        review.delete()

    return redirect('/newBook/'+str(book_id))

def deleteBook(request,id):
    if request.method=='POST':
        book=Book.objects.get(id=id)
        print book

        book.delete()

    return redirect('/homePage')


def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect('/')
