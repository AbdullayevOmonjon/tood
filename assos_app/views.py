from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def tood(request):
  data={
    'tood':Tood.objects.all()
  }
  return render(request,'todo.html',data)
