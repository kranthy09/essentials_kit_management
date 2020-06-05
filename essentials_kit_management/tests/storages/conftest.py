import pytest
from essentials_kit_management.models.models\
    import (User, Form, Section, Item, Brand,
           OrderedItem
           )
from essential_kit_management.constants.enums\
    import FormStateType


@pytest.fixture()
@pytest.mark.freeze_time('2020-12-12')
def user():
    user_object = User.create.objects(username="myname", password="myname@name123")
    return user_object

@pytest.fixture()
@pytest.mark.freeze_time('2020-12-12')
def form(user):
    form_object = Form.objects.create(
                    title = "Snacks Form",
                    description = "Contains Snacks",
                    state = FormStateType.Active.value,
                  )
    form_object.add(user)
    return form_object

@pytest.fixture()
@pytest.mark.freeze_time('2020-12-12')
def section(form):
    section_object = Section.objects.create(
                        title="Biscuits",
                        description="seciton description",
                        form=form
                     )
    return section_object
