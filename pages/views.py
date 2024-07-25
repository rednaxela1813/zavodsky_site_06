from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, DetailView
from goods.models import Category, Product
from .models import Contact
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import redirect
from .forms import ContactFormModelForm



from typing import Any




class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "pages/main/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        #context['products'] = Product.objects.all()
        context['contact'] = Contact.objects.first()

        return context
    

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'pages/main/category_products.html', {'category': category, 'products': products})

    


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'pages/main/category_details.html'
    context_object_name = 'category'



    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        # Explicitly filter products by the selected category
        context['products'] = Product.objects.filter(category=self.object)

        return context



class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/main/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


class ProductFullDescriptionView(DetailView):
    model = Product
    template_name = 'pages/main/product_full_description.html'
    context_object_name = 'product'



class ProductShortDescriptionView(DetailView):
    model = Product
    template_name = 'pages/main/product_short_description.html'
    context_object_name = 'product'



class AllDetailsProductView(DetailView):
    model = Product
    template_name = 'pages/main/all_product_details.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

# class ContactFormViews:
#     @staticmethod
#     def contact_form_view(request):
#         if request.method == 'POST':
#             form = ContactFormModelForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 # Send email to site holder
#                 send_mail(
#                     'New Contact Form Submission',
#                     f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}",
#                     'deilmann.sro@gmail.com.com',  # Replace with your email
#                     ['rednaxela1813@gmail.com'],  # Replace with the site holder's email
#                     fail_silently=False,
#                 )
#                 return redirect('success')
#         else:
#             form = ContactFormModelForm()
#         return render(request, 'pages/contact_form.html', {'form': form})

#     @staticmethod
#     def success_view(request):
#         return render(request, 'pages/success.html')


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email to site holder
            send_mail(
                'New Contact Form Submission',
                f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}",
                'deilmann.sro@gmail.com',
                ['rednaxela1813@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'pages/main/success.html')
    else:
        form = ContactFormModelForm()
    return render(request, 'pages/main/contact_form.html', {'form': form})



def contact_form_view_second(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email to site holder
            send_mail(
                'New Contact Form Submission',
                f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}",
                'deilmann.sro@gmail.com',
                ['rednaxela1813@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'pages/main/success.html')
    else:
        form = ContactFormModelForm()
    return render(request, 'pages/main/contact_form_second.html', {'form': form})

