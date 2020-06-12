import random
from django.db.models import Prefetch
from essentials_kit_management.models.models \
    import User, Item, Brand, OrderedItem
from essentials_kit_management.interactors.storages.dtos \
    import UserItemDto

def set_brand():
    brands = []
    for i in range(0,48):
        brands.append('brand_name' + f'_{i}')
    brand = random.choice(brands)
    try:
        brands.remove(brand)
    except IndexError:
        print("Index out of range")
    return brand

def set_max_quantity():
    max_qantity_list = [5,10,15,20,25]
    max_qantity = random.choice(max_qantity_list)
    return max_qantity

def set_cost_per_item():
    costs = [10,20,30,40,50,60,70,80,90,100]
    price_per_item = random.choice(costs)
    return price_per_item

def populate_brands(items):
    brand_objects = []
    for item in items:
        for i in range(3):
            brand_name = set_brand()
            min_quantity = 0
            max_quantity = set_max_quantity()
            price_per_item = set_cost_per_item()
            brand_objects.append(
                Brand(name=brand_name, 
                      min_quantity=min_quantity,
                      max_quantity=max_quantity,
                      price_per_item=price_per_item,
                      item=item
                )
            )
    Brand.objects.bulk_create(brand_objects)

    return brand_objects

def populate_orders(items):
    users \
        = list(User.objects \
                .prefetch_related(
                    Prefetch('form_set', to_attr='forms')
                    ))
    users_list = []
    orders = []
    if users:
        for user in users:
            forms = user.forms
            if forms is not None:
                users_list.append(user)
        for user in users_list:
            for item in items:
                brands = list(item.brand_set.all())
                bool_values = [True, False]
                quantity_choices = [4,5,6,7,8]
                delivered_items_choices = [2,3,4]
                brand = random.choice(brands)
                is_closed=random.choice(bool_values)
                quantity=random.choice(quantity_choices)
                delivered_items=random.choice(delivered_items_choices)
                ordered_item = OrderedItem(
                        user=user,
                        brand=brand,
                        item=item,
                        is_closed=is_closed,
                        quantity=quantity,
                        delivered_items=delivered_items
                    )
                orders.append(ordered_item)
    OrderedItem.objects.bulk_create(orders)
    return orders
