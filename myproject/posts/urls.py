from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
]
