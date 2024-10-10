from django.urls import path
from . import views

urlpatterns = [
    path('',views.function1, name='function1'),
    path('home', views.home, name='home'),
    path('index', views.index, name='index')
]