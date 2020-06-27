import datetime
import string
import factory, factory.fuzzy
from essentials_kit_management.models.models import (Form, User,
                                                     Section, Item,
                                                     Brand, OrderedItem,
                                                     SectionItem, FormUser)

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n : "username%d" % n)
    password = factory.Sequence(lambda n : "factory%d" % n)

class FormFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Form

    title = factory.Sequence(lambda n : "title%d" % n)
    description = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_letters)
    state = factory.fuzzy.FuzzyChoice(Form.Form_State_Type_choice, getter=lambda c : c[0])
    closed_date = factory.LazyFunction(datetime.datetime.now)
    expected_delivery_date = factory.LazyFunction(datetime.datetime.now)

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.users.add(user)

class SectionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Section

    title = factory.Sequence(lambda n : "title%d" % n)
    description = factory.Sequence(lambda n : "description%d" % n)
    form = factory.Iterator(Form.objects.all())

class ItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Item

    name = factory.Sequence(lambda n : "item_name%d" % n)
    item_description = factory.Sequence(lambda n : "description%d" % n)
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

    user = factory.Iterator(User.objects.all())
    item = factory.Iterator(Item.objects.all())
    brand = factory.Iterator(Brand.objects.all())
    is_closed = factory.Iterator([True, False])
    delivered_items = factory.fuzzy.FuzzyInteger(0, 10)
    quantity = factory.fuzzy.FuzzyInteger(5, 10)

class SectionItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SectionItem

    form = factory.Iterator(Form.objects.all())
    section = factory.Iterator(Section.objects.all())
    item = factory.Iterator(Item.objects.all())
    estimated_cost = factory.fuzzy.FuzzyInteger(10, 200)
    quantity_selected = factory.fuzzy.FuzzyInteger(0, 10)
    brand_selected = factory.Iterator(Brand.objects.all())

class FormUserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = FormUser

    form = factory.Iterator(Form.objects.all())
    user = factory.Iterator(User.objects.all())
    total_items = factory.fuzzy.FuzzyInteger(5, 40)
    pending_items = factory.fuzzy.FuzzyInteger(5, 10)
    cost_incurred = factory.fuzzy.FuzzyInteger(100, 500)
    total_cost_estimate = factory.fuzzy.FuzzyInteger(200, 1000)