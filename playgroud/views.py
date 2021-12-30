from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product


# Create your views here.

def say_hello(request):
    product = Product.objects.order_by("unit_price", "-title").reverse()[0]

    return render(request, "hello.html", {"name": "ayaf", "products": list(product)})
