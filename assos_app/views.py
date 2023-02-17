from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,DeleteView,FormView,UpdateView
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.models import *
from django .contrib.auth import logout, login, authenticate
# Create your views here.

def tood(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect("todo")
  data={
    'messages':Tood.objects.all(),
    'form':TodoForm()
  }
  return render(request,'todo.html',data)
# class TodoViews(View):
#   def post(self,request):
#     user=authenticate(usernam)

# class ToodCreateView(CreateView):
#   model=Tood
#   template_name='todo_creates.html'
#   fields=["nom","vaqt","batavsil","status"]

class TodoUdeta(UpdateView):
  model=Tood
  template_name='todo edt.html'
  fields=['batavsil','status']

  
def delet(request,son):
  data={
    'message':Tood.objects.get(id=son).delete()
  }
  return redirect('todo')
  
