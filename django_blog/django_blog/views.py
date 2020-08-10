from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("I am a noob project :(")
    return render(request, 'homepage.html')

def about (request):
    #return HttpResponse("hello world")
    return render(request, 'about.html')
