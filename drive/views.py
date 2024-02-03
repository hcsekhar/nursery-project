# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q

def navbar_view(request):
    navbars = Navbar.objects.all()
    return render(request, 'navbar.html', {'categories': navbars})


def category_lists(request,nav_slug):
    categories = Navbar.objects.all()
    selected_items = Items.objects.filter(navbar__slug=nav_slug)
    context = {'selected_items': selected_items}
    return render(request, 'product.html', {'context':context,'categories': categories,})


def category_list(request):
    categories = Navbar.objects.all()
    product = Items.objects.all()
    return render(request, 'navbar.html', {'categories': categories, 'product': product})


def subcategory_list(request, nav_slug):
    categories = Navbar.objects.all()
    selected_items = Items.objects.filter(category__slug=nav_slug)
    context = {'selected_items': selected_items}
    return render(request, 'product.html', context)
    # category = get_object_or_404(Navbar, nav_slug=nav_slug)
    # subcategories = Dropdown.objects.filter(category=category)
    # return render(request, 'navbar.html', {'category': category, 'subcategories': subcategories})


def product_list(request, nav_slug, item_slug):
    selected_items = Items.objects.filter(category__slug=nav_slug,subcategory__slug=item_slug)
    print(selected_items)
    context = {'selected_items': selected_items}
    return render(request, 'product.html', context)

def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products= Items.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'ecom/customer_home.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})
    return render(request,'ecom/index.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})