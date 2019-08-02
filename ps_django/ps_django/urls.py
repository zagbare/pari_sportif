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
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include, handler404, handler500
# from django.urls import include
# from django.conf import settings
# from ps_django import views



#app_name = 'ps_app'
urlpatterns = [
   
    # url(r'^contacts/$',views.contacts, name='contacts'),
    # url(r'^descriptions$',views.descriptions, name='descriptions'),
    # url(r'^$',views.home, name='home'),
    # url(r'^ps_app/',include('ps_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('ps_app.urls'))
]
# if  settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns