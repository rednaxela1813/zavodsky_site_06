from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Menu



class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "pages/main/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = Menu.objects.all()
       # context['articles'] = Article.objects.all()
        return context




