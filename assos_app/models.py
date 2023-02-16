from django.db import models

# Create your models here.

class tood(models.Model):
  nom=models.CharField(max_length=25,blank=True)
  vaqt=models.DateTimeField(blank=True)
  batavsil=models.TextField(blank=True)
  status=models.CharField(max_length=30)
  def __str__(self) -> str:
    return self.nom