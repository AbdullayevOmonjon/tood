from django.db import models

# Create your models here.

class Tood(models.Model):
  nom=models.CharField(max_length=25)
  vaqt=models.DateField()
  batavsil=models.TextField(blank=True)
  status=models.CharField(max_length=30)
  def __str__(self) -> str:
    return self.nom