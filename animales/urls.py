from django.urls import path
from . import views

urlpatterns =[
    path('home',views.index, name='home'),
    path('auspiciadores', views.auspiciadores, name='auspiciadores'),
]