from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from store.models import Product

# Create your views here.

def say_hello(request):
    product = Product.objects.filter(description__isnull=True)

    return render(request, "hello.html", {"name": "ayaf", "products": list(product)})
