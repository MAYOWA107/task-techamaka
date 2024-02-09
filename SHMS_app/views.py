from django.shortcuts import render
from django.views.generic import ListView
from .models import Hospital_Info


class Hospital_Info_View(ListView):
    model = Hospital_Info
    template_name = 'info.html'
    context_object_name = 'lists'
