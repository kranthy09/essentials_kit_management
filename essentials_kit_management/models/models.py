from django.db import models
from essentials_kit_management.constants.enums\
    import FormStateType

class Form(models.Model):
    Form_State_Type_choice = (
            (FormStateType.DONE.name, FormStateType.DONE.value),
            (FormStateType.LIVE.name, FormStateType.LIVE.value),
            (FormStateType.CLOSED.name, FormStateType.CLOSED.value)
        )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=10, choices=Form_State_Type_choice)
    closed_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField()

class FormUser(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    total_items = models.IntegerField(default=0)
    pending_items = models.IntegerField(default=0)
    cost_incurred = models.IntegerField(default=0)
    total_cost_estimate = models.IntegerField(default=0)

class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class FormSection(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)

class SectionItem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    min_quantity = models.IntegerField(default=0)
    max_quantity = models.IntegerField(default=0)
    price_per_item = models.IntegerField()

class ItemBrand(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class Order(models.Model):
    user_id = models.IntegerField()
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_cost = models.IntegerField()
    delivered_items = models.IntegerField(default=0)
    is_closed = models.BooleanField(default=False)
