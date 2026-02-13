from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def input_data(request):
    return render(request,"input.html")