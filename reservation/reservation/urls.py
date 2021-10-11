"""reservation URL Configuration

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
from django.urls import path, include
from reservation_app.views import welcome_view, admin_view, success_view, fail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', include('reservation_app.urls')),
    path('', welcome_view, name='index'),
    path('user_admin', admin_view, name='admin_view'),
    path('success', success_view, name='success_view'),
    path('fail', fail_view, name='fail_view'),

]
