from django.urls import path
from . import views



app_name = "pages"



urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
]
    

category_urlpatterns = [
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),

]

product_urlpatterns = [
    path('product/<int:pk>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/full_description/', views.ProductFullDescriptionView.as_view(), name='product_full_description'),
    path('product/<int:pk>/short_description/', views.ProductShortDescriptionView.as_view(), name='product_short_description'),
    path('product/<int:pk>/all_detail/', views.AllDetailsProductView.as_view(), name='all_product_detail'),
]

contact_urlpatterns = [
    path("contact/", views.contact_form_view, name='contact_form'),
    path('success/', views.contact_form_view, name='success'),
    path('contact_form_second/', views.contact_form_view_second, name='contact_form_second'),
]

urlpatterns = category_urlpatterns + product_urlpatterns + contact_urlpatterns + urlpatterns