from django import forms
from .models import *


class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Tood
        fields = ("nom","vaqt","batavsil","status")
