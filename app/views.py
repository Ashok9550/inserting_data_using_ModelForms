from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse 
# Create your views here.
def topic_insertion(request):
    TIO=TopicForm()
    d={'TIO':TIO}
    if request.method=='POST':
        TIOD=TopicForm(request.POST)
        if TIOD.is_valid():
            TIOD.save()
            return HttpResponse('inserted succefully .........')
    return render(request,'inserting.html',d)
def web_inseting(request):
    TIO=WebpageForm()
    d={'TIO':TIO}
    if request.method=='POST':
        TIOD=WebpageForm(request.POST)
        if TIOD.is_valid():
            TIOD.save()
            return HttpResponse('inserted succefully .........')
    return render(request,'web_inserting.html',d)
def acess_inseting(request):
    TIO=AccessForm()
    d={'TIO':TIO}
    if request.method=='POST':
        TIOD=AccessForm(request.POST)
        if TIOD.is_valid():
            TIOD.save()
            return HttpResponse('inserted succefully .........')
    return render(request,'acess_inserting.html',d)


