from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Sum,Count
from django.shortcuts import render
from store.models import Product


# Create your views here.

def say_hello(request):
    product = Product.objects.aggregate(Count("id"))
    print(product)
    return render(request, "hello.html", {"name": "ayaf"})
