import random
import pytest
from essentials_kit_management.models.models \
    import (User, Form, Section, Item, Brand,
           OrderedItem
           )
from essentials_kit_management.constants.enums \
    import FormStateType


@pytest.fixture()
@pytest.mark.freeze_time('2020-12-12')
def user():
    users = [
        User(
            username="skywaler",
            password="wallker@name123"
        ),
        User(
            username="jasper",
            password="jasper@name123"
        )
    ]
    User.objects.bulk_create(users)

@pytest.fixture()
@pytest.mark.freeze_time('2020-12-12')
def form():
    form_object = Form.objects.bulk_create(
                [
                    Form(
                        title = "Snacks Form",
                        description = "Contains Snacks",
                        state = FormStateType.LIVE.value,
                        closed_date="2020-12-12",
                        expected_delivery_date="2020-12-12"
                      ),
                      Form(
                        title = "Fruits Form",
                        description = "Contains Fruits",
                        state = FormStateType.DONE.value,
                        closed_date="2020-12-12",
                        expected_delivery_date="2020-12-12"
                      )
                ]
            )
    user_1 = User.objects.get(id=1)
    form_object = Form.objects.get(id=1)
    form_object.users.add(user_1)

@pytest.fixture()
@pytest.mark.freeze_time('2020-12-12')
def section():
    sections = [
        Section(
            title="Biscuits",
            description="contains biscuits",
            form_id=1
        ),
        Section(
            title="Chocolates",
            description="contains chocolates",
            form_id=1
        ),
        Section(
            title="Seasonal",
            description="contains seasonal",
            form_id=2
        ),
        Section(
            title="Others",
            description="contains others",
            form_id=2
        )
    ]
    Section.objects.bulk_create(sections)

@pytest.fixture()
@pytest.mark.freeze_time('2020-12-12')
def item():
    items = [
        Item(
            name="Marie Gold",
            item_description="50g",
            section_id=1
        ),
        Item(
            name="Hide and Seek",
            item_description="100g",
            section_id=1
        ),
        Item(
            name="Dairy Milk",
            item_description="40g",
            section_id=2
        ),
        Item(
            name="Bournville",
            item_description="100g",
            section_id=2
        ),
        Item(
            name="Apple",
            item_description="10pcs",
            section_id=3
        ),
        Item(
            name="Orange",
            item_description="10pcs",
            section_id=3
        ),
        Item(
            name="Grapes",
            item_description="10pcs",
            section_id=4
        ),
        Item(
            name="Mosambi",
            item_description="10pcs",
            section_id=4
        )
    ]
    Item.objects.bulk_create(items)

@pytest.fixture()
@pytest.mark.freeze_time("2020-12-12")
def brand():
    brands = []
    for item in range(1,9):
        for i in range(1,3):
            brands.append(
                    Brand(
                    name="brand_name_" + str(random.choice(list(range(16)))),
                    min_quantity=0,
                    max_quantity=10,
                    price_per_item = 60,
                    item_id=item
                )
            )
    Brand.objects.bulk_create(brands)

@pytest.fixture()
@pytest.mark.freeze_time("2020-12-12")
def ordereditem():
    orders = [
        OrderedItem(
            user_id= 1,
            item_id= 1,
            brand_id=2,
            is_closed=False,
            delivered_items=3,
            quantity=5
        ),
        OrderedItem(
            user_id=1,
            item_id=2,
            brand_id=4,
            is_closed=False,
            delivered_items=5,
            quantity=8
        ),
        OrderedItem(
            user_id=1,
            item_id=3,
            brand_id=5,
            is_closed=False,
            delivered_items=4,
            quantity=6
        ),
        OrderedItem(
            user_id= 1,
            item_id= 4,
            brand_id= 8,
            is_closed= False,
            delivered_items= 3,
            quantity= 7
        )
    ]
    OrderedItem.objects.bulk_create(orders)
