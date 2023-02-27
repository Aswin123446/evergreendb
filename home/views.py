from ast import Delete
from unicodedata import name
from urllib import response
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from product.models import fashion_collection


def index(request):
    if request.method=='POST':
        pname=request.POST['search']
        pro=fashion_collection.objects.filter(name__istartswith=pname)
    else:
        pro=fashion_collection.objects.all()
        
    
    return render(request,"index.html",{"pro":pro})
        


