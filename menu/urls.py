from django.contrib import admin
from django.urls import path
from menu.views import MenuList


urlpatterns = [
    path('',MenuList.as_view()),
    
]
