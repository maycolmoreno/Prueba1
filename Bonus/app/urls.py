from django.contrib import admin
from django.urls import path
from app.views.category.views import *

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    # path('dos/', mysecondview),
    # path('tres/', mysecondview),
]