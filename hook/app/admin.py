from django.contrib import admin

# Register your models here.
from .models import Document
# Register your models here.
@admin.register(Document)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','time','branch','message']