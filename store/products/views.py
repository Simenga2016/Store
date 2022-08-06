from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import ProductCategory, Product, Basket


# Create your views here.

def index(request):
    context = {
        'title': 'Store - main'
    }
    return render(request, 'products/index.html', context)


def products(request,category_id = None,page = 1):

    context = {
        'title': 'Store - catalog',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        product = Product.objects.filter(category_id=category_id)
    else:
        product = Product.objects.all()

    paginator = Paginator(product,6)

    products_paginator = paginator.page(page)

    context.update({'products':products_paginator})

    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id = product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)
    if not(baskets):
        basket = Basket(user = request.user, product = product,quantity=1)
        basket.save()
    else:
        basket = baskets.first()
        basket.quantity+=1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def basket_del(request, id):
    basket = Basket.objects.get(id = id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))