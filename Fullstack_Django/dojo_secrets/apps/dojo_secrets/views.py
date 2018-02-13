from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Count
import bcrypt
from .models import User,Secret

def flashErrors(request,errors):
    for error in errors:
        messages.error(request,error)


def index(request):
    return render(request,'dojo_secrets/index.html')

def success(request):
    current_user=User.objects.currentUser(request)
    secrets=Secret.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')

    for secret in secrets:
        print secret.id
        for user in secret.liked_by.all():
            print user.first_name


    context={
        'user': current_user,
        'secrets':secrets,
    }

    return render(request,'dojo_secrets/success.html', context)

def register(request):
    if request.method=='POST':
        errors=User.objects.validateUser(request.POST)
        if not errors:
            print 'Create User'
            user=User.objects.createUser(request.POST)

            request.session['user_id']=user.id

            return redirect('/success')

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

                    return redirect('/success')

            errors.append('Invalid account Information')
        flashErrors(request,errors)

    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect('/')

def postSecret(request):
    if request.method=='POST':
        if len(request.POST['content']) !=0:
            current_user=User.objects.currentUser(request)

            secret=Secret.objects.createSecret(request.POST,current_user)

    return redirect('/success')

def like(request,id):
    current_user=User.objects.currentUser(request)
    secret=Secret.objects.get(id=id)

    current_user.likes.add(secret)
    return redirect('/success')

def unlike(request,id):
    current_user=User.objects.currentUser(request)
    secret=Secret.objects.get(id=id)

    current_user.likes.remove(secret)
    return redirect('/success')

def deleteSecret(request,id):
    if request.method=='POST':
        secret=Secret.objects.get(id=id)
        current_user=User.objects.currentUser(request)

        if current_user.id==secret.author.id:
            secret.delete()
    return redirect('/success')

def mostPopular(request):
    current_user=User.objects.currentUser(request)
    secrets=Secret.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')
    context = {
        'user':current_user,
        'secrets':secrets
    }

    return render(request, 'dojo_secrets/secrets.html', context)
