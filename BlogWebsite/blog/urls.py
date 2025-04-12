from django.urls import path

from django.contrib import admin  
from . import views

urlpatterns = [
    path('/admin/', admin.site.urls),
    path('', views.main, name='main'), # make sure that the root url points to the correct view
    path('users/', views.users, name='users'),
    path('users/blog_details/<int:id>', views.blog_details, name='blog_details'),
]
