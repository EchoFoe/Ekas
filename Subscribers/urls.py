"""test_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^Subscribers/$', views.Subscribers, name='Subscribers'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^doci/$', views.doci, name='doci'),
    url(r'oprosnoi_list/$', views.oprosnoi_list, name='oprosnoi_list'),
    url(r'ekspertiza/$', views.ekspertiza, name='ekspertiza'),
    url(r'BMK/$', views.BMK, name='BMK'),
    url(r'proektirovanie/$', views.proektirovanie, name='proektirovanie'),
    url(r'kipia/$', views.kipia, name='kipia'),
    url(r'kotli/$', views.kotli, name='kotli'),
    url(r'^$', views.home, name='home'),
]