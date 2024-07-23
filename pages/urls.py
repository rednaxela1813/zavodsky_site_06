from django.urls import path

from .views import HomePageView, category_products, CategoryDetailView, ProductDetailView


app_name = "pages"



urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('category/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail')
]

