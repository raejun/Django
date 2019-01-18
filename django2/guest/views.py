from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Guest
# Create your views here.


def index(request):
    # return HttpResponse('index')
    return render(request, 'index.html')

def writeform(request):
    return render(request,'writeform.html')

def write(request):
    title = request.POST['title']
    content = request.POST['content']
    g = Guest(title=title,content=content)
    g.save()
    return redirect('/guest/list')

def list(request):
    guests = Guest.objects.all().order_by('id')
    print(guests)
    # return HttpResponse('list')
    return render(request, 'list.html',{'guests':guests})