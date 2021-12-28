from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    collections = models.ForeignKey("Collection", on_delete=models.PROTECT, related_name="collect")


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"
    MEMBERSHIP_CHOICES = ((MEMBERSHIP_BRONZE, "bronze"), (MEMBERSHIP_SILVER, "Silver"), (MEMBERSHIP_GOLD, "Gold"))
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=88, choices=MEMBERSHIP_CHOICES)
    orders = models.ForeignKey("Order", on_delete=models.PROTECT)


class Order(models.Model):
    PAYMENT_STATUS_FAILED = "F"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_CHOICES = (
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=80, choices=PAYMENT_STATUS_CHOICES)
    items = models.ForeignKey("OrderItem", on_delete=models.PROTECT, related_name="order_item")
    order = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class Collection(models.Model):
    title = models.CharField(max_length=80)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Card(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
