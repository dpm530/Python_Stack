from django.shortcuts import render
from .models import User,Message,Comment

def index(request):
    return render(request,'first_app/index.html')
