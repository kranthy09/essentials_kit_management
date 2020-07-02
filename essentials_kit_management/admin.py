# your django admin
from django.contrib import admin
from essentials_kit_management.models.models\
    import Form, Section, Item, Brand, OrderedItem


admin.site.register(Form)
admin.site.register(Section)
admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(OrderedItem)