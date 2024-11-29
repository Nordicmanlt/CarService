from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('ser/', views.services, name='ser'),

]