from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse

def index(request):
    return HttpResponse('this is my web test')
def myblog(request):
    return render(request,'Myapp/index.html')
