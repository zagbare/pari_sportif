"""ps_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url

# from django.views.generic import TemplateView
# from . import views

# app_name = 'ps_app'
# urlpatterns = [
# 	url(r'^$',views.index, name='index'),
#     url(r'^list$', views.list, name='list'),
#     url(r'^Articles/(?P<id>[0-9]+)$', views.details, name='details'),
#     url(r'^static/',TemplateView.as_view(template_name='ps_app/static.html')),
#     url(r'^connection/',TemplateView.as_view(template_name = 'ps_app/login.html')),
#     url(r'^login/', views.login, name= 'login'),
#     url(r'^profile/',TemplateView.as_view(template_name = 'ps_app/profile.html')), 
#     url(r'^saved/', views.SaveProfile, name = 'saved'),
#     url(r'^connection/',views.formView, name = 'loginform'),
#     url(r'^logout/',views.logout, name = 'logout'),
# ]
#  

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    contacts = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)


class Paries(models.Model):
    equipeA = models.CharField(max_length=100, null=True,unique=True)
    score = models.CharField(max_length=100, verbose_name="scoreA",null=True)
    scoreB = models.CharField(max_length=100, null=True)
    equipeB = models.CharField(max_length=100, null=True,unique=True)
    montant_parié = models.CharField(max_length=100,null=True)
    date_match = models.DateField(null=True)
    v_date_match = models.CharField(max_length=100, null=True)
    date_parie = models.DateTimeField(auto_now_add=True,null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_parie", null=True)