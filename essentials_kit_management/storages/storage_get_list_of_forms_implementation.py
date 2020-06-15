from django.db.models import Prefetch
from .decorator import profile
from essentials_kit_management.interactors.storages.dtos \
    import (FormDto,
           GetFormDto,
           UserItemDto,
           UserBrandDto,
           ItemBrandDto,
           FormSectionDto,
           SectionItemDto
         )
from essentials_kit_management.models.models\
    import User, Form, Section, Item, Brand, OrderedItem
from essentials_kit_management.interactors.storages\
    .storage_list_of_forms_interface \
        import StorageListOfFormsInterface
from essentials_kit_management.exceptions.exceptions\
    import InvalidUsername, InvalidPassword
from typing import List


class StorageListOfFormsImplementation(StorageListOfFormsInterface):

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

    def get_list_of_form_dtos(self,
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
                        delivery_date=str(form_object.expected_delivery_date.date()),
                        closing_date=str(form_object.closed_date.date())
                    )
                )
        return form_dtos

    def get_user_item_dtos(self, user_id: int,
                     form_ids: List[int]
                    )-> List[UserItemDto]:
        user_item_dtos = []
        user = User.objects.get(id=user_id)
        forms = user.form_set.all()
        for form in forms:
            sections = form.section_set.all()
            for section in sections:
                items = section.item_set.all()
                for item in items:
                    user_item_dto \
                        = UserItemDto(
                                form_id=form.id,
                                user_id=user_id,
                                item_id=item.id
                            )
                    user_item_dtos.append(user_item_dto)
        return user_item_dtos

    def get_user_brand_dtos(self, 
                            user_id: int,
                            item_ids: List[int]
                        )-> List[UserBrandDto]:
        orders = OrderedItem.objects.filter(user_id=user_id).select_related('brand', 'item')
        user_brand_dtos = []
        for order in orders:
            user_brand_dtos.append(
                UserBrandDto(
                    brand_id=order.brand.id,
                    item_id=order.item.id,
                    max_quantity=order.brand.max_quantity,
                    quantity=order.quantity,
                    price_per_item=order.brand.price_per_item,
                    delivered_items=order.delivered_items,
                    is_closed=order.is_closed
                )
            )
        return user_brand_dtos