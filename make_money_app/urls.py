from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('process_money', views.process_money),
]