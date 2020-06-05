from .decorator import profile
from essentials_kit_management.interactors.storages.dtos \
    import FormDto
from essentials_kit_management.models.models\
    import User, Form, Section, Item, Brand, OrderedItem
from essentials_kit_management.interactors.storages\
    .storage_interface import StorageInterface
from essentials_kit_management.exceptions.exceptions\
    import InvalidUsername, InvalidPassword
from typing import List


class StorageImplementation(StorageInterface):

    def validate_username(self,
                          username:str):
        try:
            User.objects.get(username=username)
        except User.ObjectDoesnotExists:
            raise InvalidUsername

    def validate_username_and_password(self,
                                       username: str,
                                       password: str
                                      ):
        try:
            user_id = User.objects.get(
                            username=username,
                            password=password
                      )
        except User.ObjectDoesnotExists:
            raise InvalidPassword

        return user_id

    def get_list_of_form_dtos(self, user_id: int,
                              offset: int, limit: int
                             )-> List[FormDto]:
        form_dtos = []
        form_objects = Form.objects.all()[offset:offset+limit]
        for form_object in form_objects:
            form_dtos.append(
                    FormDto(
                        form_id=form_object.id,
                        form_name=form_object.title,
                        form_state=form_object.state,
                        delivery_date=form_object.expected_delivery_date,
                        closing_date=form_object.closed_date
                    )
                )
        return form_dtos

    def get_user_item_dtos(self,
                           user_id: int,
                           form_ids: List[int]
                    )-> List[UserItemDto]:
        order_items = OrderedItem.objects.filter(user_id=user_id)
        for order_item in order_items:
            user_item_dtos.append(
                    form_ids
                )