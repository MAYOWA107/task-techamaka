from django.contrib import admin
from .models import Hospital_Info


class ModelAdmin(admin.ModelAdmin):
    fields = '__all__'
    

admin.site.register(Hospital_Info)

