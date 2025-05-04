from django.contrib import admin 
from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.index, name='home'),
    path('menu-items/', views.MenuItemView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)


]