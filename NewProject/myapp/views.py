from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('this is a web site')

def detail(request,num):
    return  HttpResponse('detail--{}'.format(num))

def love(request):
    return HttpResponse('I Love U')

from .models import Grades,Students
def grades(request):
    #去模版里面取数据
    gradesList = Grades.objects.all()
    #把数据给模版
    return render(request,'myapp/grades.html',{'grades':gradesList})
def students(request):
    studentsList = Students.objects.all()
    return render(request,'myapp/students.html',{'students':studentsList})