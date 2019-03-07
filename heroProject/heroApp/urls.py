from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('apply/', views.application, name="application"),
    path('newform/', views.newform, name ="newform"),
    path('welcome/', views.welcome, name="welcome"),


]