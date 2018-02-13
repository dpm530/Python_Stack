from django.shortcuts import render,redirect
from .models import User

def index(request):

    return render(request,'first_app/index.html')

def success(request):
    if 'user_id' in request.session:
        user_id=request.session['user_id']
        context={
            'current_user':User.objects.get(id=user_id)
        }

        return render(request,'first_app/success.html', context)
    return redirect('/')

def create(request):

    if request.method=='POST':
        check=User.objects.validate(request.POST)
        if check:
            print check
            return redirect('/')

        user=User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'], password=request.POST['password'])

        request.session['user_id']=user.id

        return redirect('/success')

    return redirect('/')

def logout(request):
    request.session.pop('user_id')

    return redirect('/')

def login(request):
    if request.method=='POST':
        form_data=request.POST
        check=User.objects.validate_login(form_data)

        if check:
            print check
            return redirect('/')

        user=User.objects.filter(email=form_data['email']).first()

        if user:
            if str(form_data['password'])==user.password:
                request.session['user_id']=user.id
                return redirect('/success')

    return redirect('/')
