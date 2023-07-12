from django.shortcuts import render
from menu.models import Menu,Category
from django.views import generic
# Create your views here.

class MenuList(generic.ListView):
    model= Menu
