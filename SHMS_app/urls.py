from django.urls import path
from .views import Hospital_Info_View



urlpatterns = [
    path('info/', Hospital_Info_View.as_view(), name='info'),
]
