from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
    path('update/<int:task_id>/', task_update, name='task_update'),

]
