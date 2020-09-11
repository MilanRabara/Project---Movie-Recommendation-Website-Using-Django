from django.urls import path
from . import views
from django.contrib.auth import views as view

urlpatterns = [
    path('', views.home_page, name="home"),
    path('home/', views.page, name="page"),
    path('signup/', views.sign_up, name="sign-up"),
]
