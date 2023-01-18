from django.shortcuts import render, redirect, HttpResponse
from .models import human
from django.views.decorators.csrf import csrf_exempt



def index(request) :
  return render(request, "folder/index.html")

def create(request) :
  name = request.GET.get("name")
  age = request.GET.get("age")
  humans = human(name=name, age = age)
  humans.save()
  return render(request,"folder/index.html")

# @csrf_exempt
# def read(request) :
#   global topics


# @csrf_exempt
# def update(request) :

  # return render(request, "folder/update.html")

def read(request):
  humans = human.objects.all()
  context ={
    "humans" : humans
  }
  return render(request, "folder/index.html", context)

def delete(request):
  b = human.objects.all()
  b.delete()
  return render(request,"folder/index.html")

def main(request) :
  return render(request, "folder/main.html")

def sub(request):
  return render(request, "folder/sub.html")

def three(request):
  return render(request, "folder/three.html")

def four(request): 
  return render(request, "folder/four.html")
