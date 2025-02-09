
from django.urls import path
from .views import *
urlpatterns = [
    path('', home_page, name='home'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('update/<int:post_id>/', post_update, name='post_update'),
    path('delete/<int:post_id>/', post_delete, name='post_delete'),
    path('category/<int:post_id>/', category_view, name='category_view')


]
