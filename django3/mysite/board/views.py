from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Board

def index(request):
    return render(request, 'board/index.html')


def writeform(request):
    return render(request, 'board/writeform.html')

def write(request):
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    pwd = request.POST['password']
    b = Board(title=title, content=content, writer=writer, pwd=pwd)
    b.save()
    return HttpResponse("저장 성공!")

def list(request):
    lists = Board.objects.all().order-by('-id')
    print(lists)
    return render(request, 'board/list.html', {'lists':lists})

def read(request, post_id):
    b = Board.objects.get(id=post_id)
    b.hit = b.hit + 1
    b.save() # update
    return render(request, 'board/read.html', {'b':b})