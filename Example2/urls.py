from django.contrib import admin
from django.urls import path, re_path 
from django.conf.urls import include
from django.contrib.auth.models import User

from Example2.views import ExampleList

urlpatterns = [
    re_path(r'/example2/$', ExampleList.as_view()),
]
