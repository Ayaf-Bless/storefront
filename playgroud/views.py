from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from store.models import Product

# Create your views here.

def say_hello(request):

    is_set = Product.objects.filter(pk=0).exists()


    return render(request, "hello.html", {"name": "ayaf", })
