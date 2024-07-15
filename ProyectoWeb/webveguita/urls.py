#from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from  . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria/', views.galeria, name='galeria'),
    path('opinion/', views.opinion, name='opinion'),
    path('quienes/', views.quienes, name='quienes'),
    path('solicitar/', views.solicitar, name='solicitar'),
    path('base/', views.base, name='base'),
    path('registro/', views.registro, name='registro'),
    path('compra/',views.compra, name='compra'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]