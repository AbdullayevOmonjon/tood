from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,DeleteView
from .models import *
# Create your views here.

def tood(request):
  data={
    'messages':Tood.objects.all()
  }
  return render(request,'todo.html',data)

class ToodCreateView(CreateView):
  model=Tood
  template_name='todo.html'
  fields=["nom","vaqt","batavsil","status"]
  
def delet(request,son):
  data={
    'message':Tood.objects.get(id=son).delete()
  }
  return redirect('todo')
  
