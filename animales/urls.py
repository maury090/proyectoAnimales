from django.urls import path
from . import views

urlpatterns =[
    path('home',views.index, name='home'),
    path('auspiciadores', views.auspiciadores, name='auspiciadores'),
    path('apadrinacion', views.apadrinacion, name='apadrinacion'),
    path('adopcionP',views.adopcionP, name='adopcionP'),
    path('adopcionP2',views.adopcionP2, name='adopcionP2'),
    path('adopcionG', views.adopcionG, name='adopcionG')
]