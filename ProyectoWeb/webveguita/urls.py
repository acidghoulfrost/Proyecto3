#from django.conf.urls import url
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria/', views.galeria, name='galeria'),
    path('opinion/', views.opinion, name='opinion'),
    path('quienes/', views.quienes, name='quienes'),
    path('solicitar/', views.solicitar, name='solicitar'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
]