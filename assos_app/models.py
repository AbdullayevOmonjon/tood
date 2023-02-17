from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Tood(models.Model):
  nom=models.CharField(max_length=25)
  vaqt=models.DateTimeField()
  batavsil=models.TextField(blank=True)
  status=models.BooleanField(blank=True)
  def __str__(self) -> str:
    return self.nom
  
  def get_absolute_url(self):
      return reverse("todo")
  

  