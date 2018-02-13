from django.shortcuts import render
from datetime import datetime

def index(request):
    date = datetime.now()
    print date
    context = {
         'date':date,
     }
    return render(request,'first_app/index.html',context)
