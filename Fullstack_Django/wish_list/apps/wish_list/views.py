from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt
from .models import User,WishList

def showErrors(request,errors):
    for error in errors:
        messages.error(request,error)

def index(request):

    return render(request,'wish_list/index.html')

def homePage(request):
    current_user=User.objects.currentUser(request)
    created_wishlists=current_user.list_items.all()
    joined_wishlists=current_user.other_wish_lists.all()
    other_wishlists=WishList.objects.exclude(id__in=created_wishlists).exclude(id__in=joined_wishlists)

    context={
        'user': current_user,
        'created_wishlists': created_wishlists,
        'joined_wishlists':joined_wishlists,
        'other_wishlists':other_wishlists,
    }

    return render(request,'wish_list/homePage.html',context)

def register(request):
    if request.method=='POST':
        errors=User.objects.validateUser(request.POST)
        if not errors:
            user=User.objects.createUser(request.POST)
            request.session['user_id']=user.id

            return redirect('/homePage')

        showErrors(request,errors)
    return redirect('/')

def login(request):
    if request.method=='POST':
        errors=User.objects.validateLogin(request.POST)

        if not errors:
            user=User.objects.filter(username=request.POST['username']).first()

            if user:
                password=str(request.POST['password'])
                user_password=str(user.password)

                hashed_pw=bcrypt.hashpw(password,user_password)

                if hashed_pw==user_password:
                    request.session['user_id']=user.id

                    return redirect('/homePage')

            errors.append('Invalid Account Information!')

        showErrors(request,errors)

    return redirect('/')

def logout(request):
    if 'user_id' in session:
        request.session.pop('user_id')

    return redirect('/')

def addItemPage(request):
    return render(request,'wish_list/addItemPage.html')

def addItem(request):
    if request.method=='POST':
        errors=WishList.objects.validateItem(request.POST)

        if not errors:
            current_user=User.objects.currentUser(request)
            items=WishList.objects.createListItem(request.POST, current_user)

            return redirect('/homePage')

        showErrors(request,errors)

    return redirect('/addItemPage')

def deleteItem(request,item_id):
    if request.method=='POST':
        listitem=WishList.objects.get(id=item_id)

        listitem.delete()


    return redirect('/homePage')

def removeItem(request,item_id):
    if request.method=='POST':
        current_user=User.objects.currentUser(request)
        listitem=WishList.objects.get(id=item_id)

        current_user.other_wish_lists.remove(listitem)


    return redirect('/homePage')

def addItem(request,item_id):
    if request.method=='POST':
        current_user=User.objects.currentUser(request)
        listitem=WishList.objects.get(id=item_id)

        current_user.other_wish_lists.add(listitem)

    return redirect('/homePage')

def item(request,id):
    item=WishList.objects.get(id=id)
    user=item.users.all()

    context={
        'items':item,
        'users':user,
    }

    return render(request,'wish_list/item.html',context)
