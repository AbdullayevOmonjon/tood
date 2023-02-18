from django.urls import path
from .views import *

urlpatterns = [
   path('',loginview,name='loginwiew'), 
   path('todo/',tood,name='todo'),
   path('delet/<int:son>',delet,name='delet'),
   path('todo/update/<int:pk>',TodoUdeta.as_view(),name='update')
]