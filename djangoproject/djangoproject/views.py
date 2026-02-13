from django.http import HttpResponse
from django.shortcuts import render

from app.models import Student

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def input_data(request):
    return render(request,"input.html")

def student_data(request):
    students = Student.objects.all()
    return render(request,'student.html', {'students': students})