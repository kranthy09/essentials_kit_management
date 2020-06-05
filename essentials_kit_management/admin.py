# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from essentials_kit_management.models.models\
    import User, Form, Section, Item, Brand, OrderedItem


admin.site.register(User, UserAdmin)
admin.site.register(Form)
admin.site.register(Section)
admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(OrderedItem)