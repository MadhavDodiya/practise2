
from django.http import HttpResponse
from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.


def home(request):
    return render(request, 'index.html')


def data1(request):
    a=request.POST.get('name')
    b=request.POST.get('pas')
    
    obj=data(name=a,password=b)
    obj.save()
    
    return redirect('/')

def display(request):
    obj=data.objects.all()
    return render(request , 'display.html' , {'data':obj})

def delete(request):
    a=request.POST.get('id')
    
    obj=data.objects.filter(id=a)
    obj.delete()
    
    return redirect('/display')

def update(request):
    
    a=request.POST.get('id')

    d=data.objects.filter(id=a)
    return render(request,'update.html',{'obj':d})

def newdata(request):
    a=request.POST.get('name')
    b=request.POST.get('pas')
    
    c=request.POST.get('id')
    obj=data.objects.get(id=c)
    obj.name=a
    obj.password=b
    obj.save()
    
    return redirect('/display')

