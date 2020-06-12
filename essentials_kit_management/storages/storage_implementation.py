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
        user_brand_dto = []
        for order in orders:
            user_brand_dto.append(
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
        return user_brand_dto
    
    def get_form_dto(self,
                     user_id: int,
                     form_id: int
                    )-> GetFormDto: 
        form = Form.objects.get(id=form_id)
        form_dto = GetFormDto(
                      form_id=form_id,
                      form_name=form.title,
                      form_state=form.state,
                      form_description=form.description,
                      closing_date=form.closing_date
                   )
        return form_dto

    def get_form_section_dtos(
                    self,
                    form_id: int
            )-> List[FormSectionDto]:
        form = Form.objects.filter(id=form_id) \
                .prefetch_related(
                    Prefetch('section_set', to_attr='sections')
                )
        for form_object in form:
            sections = form_object.sections
        form_section_dtos = []
        for section in sections:
            form_section_dtos.append(
                FormSectionDto(
                    form_id=form_id,
                    section_id=section.id,
                    section_title=section.title,
                    section_description=section.description
                )
            )
        return form_section_dtos

    def get_section_item_dtos(
                self,
                section_ids: List[int]
            )-> List[SectionItemDto]:
        sections \
            = Section.objects\
                .filter(id__in=section_ids).prefetch_related(
                        Prefetch('item_set', to_attr='items')
                )
        section_item_dtos = []
        for section in sections:
            items = section.items
            for item in items:
                section_item_dtos.append(
                    SectionItemDto(
                        section_id=section.id,
                        item_id=item.id,
                        item_name=item.name,
                        item_description=item.item_description
                    )
                )
        return section_item_dtos
        

    def get_item_brand_dtos(
                self,
                item_ids: List[int]
            )-> List[ItemBrandDto]:
        items \
            = Item.objects \
                .filter(id__in=item_ids) \
                    .prefetch_related(Prefetch('brand_set', to_attr='brands'))
        item_brand_dtos = []
        for item in items:
            brands = item.brands
            for brand in brands:
                item_brand_dtos.append(
                    ItemBrandDto(
                        item_id=item.id,
                        brand_id=brand.id,
                        brand_name=brand.name,
                        min_quantity=brand.min_quantity,
                        max_quantity=brand.max_quantity,
                        price=brand.price_per_item
                    )
                )
        return item_brand_dtos

    def get_order(self, user_id: int,
                  item_id: int, brand_id: int
                )-> bool:
        pass

    def update_order(self, user_id: int,
                     item_brand_dto: ItemBrandDto
                    ):
        pass

    def create_order(self, user_id: int,
                     item_brand_dto: ItemBrandDto
                    ):
        pass