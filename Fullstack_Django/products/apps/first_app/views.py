from django.shortcuts import render
from .models import Product

def index(request):

    return render(request,'first_app/index.html')
