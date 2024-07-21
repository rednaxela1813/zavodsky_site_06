from django.urls import path
from .views import SPAView, category_products


app_name = 'goods'


urlpatterns = [
   # path('', HomePageView.as_view(), name='home'),
    path('', SPAView.as_view(), name='spa'),
    path('category/<int:category_id>/', category_products, name='category_products'),

]

