import factory.fuzzy
import factory
import string
import datetime
from .models import (Form, Section,
                    Item, Brand, FormUser,
                    OrderedItem, SectionItem)


class FormFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Form

    title = factory.fuzzy.FuzzyText(length=6, chars=string.ascii_letters)
    description = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_letters)
    state = factory.fuzzy.FuzzyChoice(Form.Form_State_Type_choice, getter=lambda c: c[0])
    closed_date = factory.LazyFunction(datetime.datetime.now)
    expected_delivery_date = factory.LazyFunction(datetime.datetime.now)

class SectionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Section

    title = factory.fuzzy.FuzzyText(length=6, chars=string.ascii_letters)
    description = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_letters)
    form = factory.Iterator(Form.objects.all())

class ItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Item

    name = factory.Sequence(lambda n : "name%d" % n)
    item_description = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_letters)
    section = factory.Iterator(Section.objects.all())

class BrandFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Brand

    name = factory.Sequence(lambda n : "brand_name%d" % n)
    min_quantity = factory.fuzzy.FuzzyInteger(0)
    max_quantity = factory.fuzzy.FuzzyInteger(15)
    price_per_item = factory.fuzzy.FuzzyInteger(40, 100)
    item = factory.Iterator(Item.objects.all())

class OrderedItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = OrderedItem

    item = factory.Iterator(Item.objects.all())
    brand = factory.Iterator(Brand.objects.all())
    user_id = factory.Sequence(lambda n : "%d" % n)
    is_closed = factory.Iterator([False, True])
    delivered_items = factory.fuzzy.FuzzyInteger(10)
    quantity = factory.fuzzy.FuzzyInteger(10)

class SectionItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SectionItem
    form = factory.Iterator(Form.objects.all())
    section = factory.Iterator(Section.objects.all())
    item = factory.Iterator(Item.objects.all())
    estimated_cost = factory.fuzzy.FuzzyInteger(500)
    quantity_selected = factory.fuzzy.FuzzyInteger(10)
    brand_selected = factory.Sequence(lambda n : "brand%d" % n)

class FormUserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = FormUser

    form = factory.Iterator(Form.objects.all())
    user_id = factory.Sequence(lambda n : "%d" % n)
    total_items = factory.fuzzy.FuzzyInteger(30)
    pending_items = factory.fuzzy.FuzzyInteger(5)
    cost_incurred = factory.fuzzy.FuzzyInteger(500)
    total_cost_estimate = factory.fuzzy.FuzzyInteger(500)
