# your django admin
from django.contrib import admin
from essentials_kit_management.models.models\
    import (Form, FormUser,
            Section, SectionItem,
            FormSection, Item,
            Brand, ItemBrand, Order)


admin.site.register(Form)
admin.site.register(FormUser)
admin.site.register(Section)
admin.site.register(SectionItem)
admin.site.register(FormSection)
admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(ItemBrand)
admin.site.register(Order)
