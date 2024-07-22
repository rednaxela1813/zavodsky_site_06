from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView




class HomePageView(TemplateView):
    template_name = "pages/main/index.html"
    
    




