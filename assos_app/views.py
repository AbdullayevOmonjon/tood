from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,DeleteView
from .models import *
from .forms import *
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

# class ToodCreateView(CreateView):
#   model=Tood
#   template_name='todo_creates.html'
#   fields=["nom","vaqt","batavsil","status"]
  
def delet(request,son):
  data={
    'message':Tood.objects.get(id=son).delete()
  }
  return redirect('todo')
  
