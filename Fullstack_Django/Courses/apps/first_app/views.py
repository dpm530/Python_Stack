from django.shortcuts import render,redirect
from .models import Course

def index(request):
    context={
        'courses':Course.objects.all()
    }

    return render(request,'first_app/index.html',context)

def post(request):
    Course.objects.create(name=request.POST['name'],description=request.POST['description'])

    return redirect('/')

def confirm(request,id):
    course=Course.objects.get(id=id)
    context={
        'course':course
    }

    return render(request,'first_app/delete.html',context)

def delete(request,id):
    Course.objects.get(id=id).delete()

    return redirect('/')
