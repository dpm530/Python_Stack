from django.shortcuts import render

def index(request):
    return render(request, 'first_app/index.html')

def testimonial(request):
    return render(request,'first_app/testimonials.html')
