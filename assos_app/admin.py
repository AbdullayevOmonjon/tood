from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Tood)
class ToodAdmin(admin.ModelAdmin):
  list_display=('id','nom','vaqt','batavsil','status')
  list_editable=('status','vaqt')
  list_display_links=('nom',)
  list_filter=('nom','vaqt','status')
  search_fields=('nom','id')
  
  

