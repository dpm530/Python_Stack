from django.shortcuts import render

def index(request):
    return render(request,'first_app/index.html')

def about(request):
    return render(request,'first_app/about.html')

def project(request):
    return render(request,'first_app/projects.html')

def testimonial(request):
    return render(request,'first_app/testimonials.html')
