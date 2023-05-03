"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from jenkinsapi import views

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/CI/build/start', views.build_start),
    path('api/CI/build/start/sub', views.build_start_sub),
    path('api/CI/build/log', views.build_log),
    path('api/CI/build/status', views.build_status_sub),
    path('api/CI/build/stop', views.build_stop),
    path('api/CI/build/stop/sub', views.build_stop_sub),


    path('post/', views.post),
    path('initialize/', views.initialize),


    
    
    
    # path('', TemplateView.as_view(template_name'index.html')),
]



