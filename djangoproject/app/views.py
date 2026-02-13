from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    return render(request,"login.html")

def input_data(request):
    return render(request,"input.html")

def student_data(request):
    students = Student.objects.all()
    return render(request,'student.html', {'students': students})