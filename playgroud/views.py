from typing import Collection
from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Cart, CartItem, Customer, Order, OrderItem, Product, Collection
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

# Create your views here.


def say_hello(request):
    return render(request, "hello.html", {"name": "mosh", })
