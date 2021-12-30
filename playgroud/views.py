from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
from store.models import Product


# Create your views here.

def say_hello(request):
    product = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))

    return render(request, "hello.html", {"name": "ayaf", "products": list(product)})
