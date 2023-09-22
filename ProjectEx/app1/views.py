from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *
import datetime
# Create your views here.


def home(request):
    dt = datetime.datetime.now()
    return render(request, 'home.html',{'dt':dt})

def signup(request):
    dt = datetime.datetime.now()
    if request.method == 'POST':
        fm = Signup(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            add = fm.cleaned_data['address']
            res = Userinfo(name=nm, email=em, address=add)
            res.save()
            return HttpResponseRedirect('/home/')
    else:
        fm = Signup()
    return render (request, 'signup.html', {'form':fm, 'dt':dt})

def weather(request):
    dt = datetime.datetime.now()
    return render(request, 'weather.html', {'dt':dt})

def show(request):
    data = Userinfo.objects.all()
    return render(request, 'show.html',{'data':data})