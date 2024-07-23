from django.urls import path
from . import views



app_name = "pages"



urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('product/<int:pk>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/full_description/', views.ProductFullDescriptionView.as_view(), name='product_full_description'),
    path('product/<int:pk>/short_description/', views.ProductShortDescriptionView.as_view(), name='product_short_description'),
]


