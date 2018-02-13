from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse


def index(request):
    return render(request,'first_app/index.html')

def process(request):
    if User.objects.validation(request.POST['user']):
        User.objects.create(username=request.POST['user'])
        messages.success(request, 'The email address you entered '+request.POST['user']+' is valid!')
        return redirect(reverse('success'))
    else:
        messages.warning(request,'Invalid email!!')
        return redirect(reverse('index'))

def success(request):
    context={
        'users':User.objects.all()
    }
    return render(request,'first_app/success.html',context)
