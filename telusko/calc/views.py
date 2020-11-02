from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {"name": "Somsubhra Das"})


def add(request):
    result = int(request.POST["num1"]) + int(request.POST["num2"])
    return render(request, "result.html", {"result": result})
