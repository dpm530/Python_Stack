from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if not 'count' in request.session:
        request.session['count']=1
    return render(request,'first_app/index.html')

def result(request):
    print "*"*50
    return render(request,'first_app/result.html')

def process(request):

    if request.method == "POST":

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['count'] += 1

        return redirect('/result')
