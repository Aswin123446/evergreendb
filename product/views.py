from functools import cache
from re import T
from unicodedata import name

import django
from.models import comment_box, fashion_collection
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.core.cache import cache




def details2(request):
    id=request.GET['id']
    pro=fashion_collection.objects.get(id=id)
    if 'recent' in request.session:
        print(request.session['recent'])
        if id in request.session['recent']:
            request.session['recent'].remove(id)
        if len(request.session['recent'])> 4:
            request.session['recent'].pop()
        van=fashion_collection.objects.filter(id__in=request.session['recent'])
            
        request.session['recent'].insert(0,id)
    else:
        request.session['recent']=[id] 
        van=fashion_collection.objects.filter(id=id)
    request.session.modified=True

    pro=fashion_collection.objects.get(id=id)
    return render(request,"about.html", {'key1':pro,'van':van})


    
def comment(request):
        name=request.POST['user']
        id=request.POST['pro']
        message=request.POST['msg']
        cmt=comment_box.objects.create(name=name,msg=message,fkey_id=id)
        cmt.save();
        return redirect("/")


    
