# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def navbar_view(request):
    navbars = Navbar.objects.all()
    return render(request, 'navbar.html', {'categories': navbars})


def category_list(request):
    categories = Navbar.objects.all()
    product = Items.objects.all()
    return render(request, 'navbar.html', {'categories': categories, 'product': product})


def subcategory_list(request, nav_slug):
    selected_items = Items.objects.filter(category__slug=nav_slug)
    context = {'selected_items': selected_items}
    return render(request, 'basedonslug.html', context)
    # category = get_object_or_404(Navbar, nav_slug=nav_slug)
    # subcategories = Dropdown.objects.filter(category=category)
    # return render(request, 'navbar.html', {'category': category, 'subcategories': subcategories})


def product_list(request, nav_slug, item_slug):
    selected_items = Items.objects.filter(category__slug=nav_slug,subcategory__slug=item_slug)
    print(selected_items)
    context = {'selected_items': selected_items}
    return render(request, 'basedonslug.html', context)
