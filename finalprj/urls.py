"""finalprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from finalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.profile_view, name='Home'),
    path('register/', views.register, name='register'),
    path('', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('no_ceaser/', views.no_ceaser, name='no_ceaser' ),
    path('pagetwo/', views.profile_view2, name='pagetwo' ),
    path('pageone/', views.a_input, name='pageone' ),
]
