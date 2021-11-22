from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('uno/', myfirstview),
    path('dos/', mysecondview),
    path('tres/', mysecondview),
]