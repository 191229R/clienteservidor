from django.contrib import admin
from django.urls import path, re_path 
from django.conf.urls import include
from django.contrib.auth.models import User

from Example1.views import ExampleList

urlpatterns = [
    re_path(r'/example1/$', ExampleList.as_view()),
]
