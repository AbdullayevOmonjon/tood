from django.urls import path
from .views import *

urlpatterns = [
   path('',tood,name='todo'),
   path('delet/<int:son>',delet,name='delet'),
   path('todo/update/<int:pk>',TodoUdeta.as_view(),name='update')
   # path( 'todo_creat/', ToodCreateView.as_view(),name='todo_creat')
]