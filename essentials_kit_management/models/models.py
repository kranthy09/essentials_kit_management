from django.contrib.auth.models import AbstractUser
from django.db import models
from essentials_kit_management.constants.enums\
    import FormStateType


class User(AbstractUser):
    username = models.TextField(unique=True)
    password = models.TextField()

class Form(models.Model):
    Form_State_Type_choice = (
            (FormStateType.Done.name, FormStateType.Done.value),
            (FormStateType.Live.name, FormStateType.Live.value),
            (FormStateType.Closed.name, FormStateType.Closed.value)
        )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=10, choices=Form_State_Type_choice)
    closed_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField()
    users = models.ManyToManyField(User)

class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    min_quantity = models.IntegerField(default=0)
    max_quantity = models.IntegerField(default=0)
    price_per_item = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class OrderedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_closed = models.BooleanField(models.Model)
    delivered_items = models.IntegerField(default=0)
    quantity = models.IntegerField()

class SectionItem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    estimated_cost = models.IntegerField(default=0)
    quantity_selected = models.IntegerField(default=0)
    brand_selected = models.CharField(max_length=100, default='brand')