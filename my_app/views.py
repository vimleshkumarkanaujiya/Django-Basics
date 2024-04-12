from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<h1>Hi Metteyya</h1>")

def about(request):
    return HttpResponse("<h1>About Me</h2>")

def greet(request, first_name):
    return HttpResponse(f"<h1>Hi, {first_name}</h1>")

def add(request, n1, n2):
    return HttpResponse(f"<h1>The addition is: {n1+n2}</h1>")