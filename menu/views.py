from django.shortcuts import render
from menu.models import Menu
from django.views import generic
# Create your views here.

class MenuList(generic.ListView):
    model= Menu
    
    
    def get_context_data(self, **kwargs):
        context = super(MenuList, self).get_context_data(**kwargs)
        context['starter'] = Menu.objects.filter(category='starter')
        context['breakfast'] = Menu.objects.filter(category='breakfast')
        context['lunch'] = Menu.objects.filter(category='lunch')
        context['dinner'] = Menu.objects.filter(category='dinner')
        return context