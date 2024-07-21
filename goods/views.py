from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Product
from typing import Any
from django.shortcuts import get_object_or_404



class SPAView(TemplateView):
    template_name = 'pages/main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
       # context['contact'] = Contact.objects.first()

        return context
    

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'pages/main/category_products.html', {'category': category, 'products': products})


