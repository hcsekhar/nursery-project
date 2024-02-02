# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('navbar/', navbar_view, name='navbar'),
    path('categories/', category_list, name='category_list'),
    path('categories/<slug:nav_slug>/', subcategory_list, name='subcategory_list'),
    path('categories/<slug:nav_slug>/<slug:item_slug>', product_list, name='product_list')

    # Add other paths as needed
]
