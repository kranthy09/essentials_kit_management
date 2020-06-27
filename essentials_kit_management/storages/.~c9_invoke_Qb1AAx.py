from django.db.models import Prefetch
from .decorator import profile
from essentials_kit_management.interactors.storages.dtos \
    import (FormDto,
           GetFormDto,
           UserItemDto,
           UserBrandDto,
           ItemBrandDto,
           FormSectionDto,
           SectionItemDto,
           ItemBrandsDto,
           BrandDetailsDto,
           SectionItemsDto,
           ItemDetailsDto
         )
from essentials_kit_management.models.models\
    import User, Form, Section, Item, Brand, OrderedItem
from essentials_kit_management.interactors.storages\
    .storage_interface \
        import StorageInterface
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

    def validate_form_id(self, form_id: int):
        is_form_id_exists = Form.objects.get(id=form_id).exists()
        if is_form_id_exists:
            return True
        else:
            return False

    def get_valid_item_ids(self, item_ids: List[int])-> \
        List[int]:

        valid_item_ids = []
        for item_id in item_ids:
            is_item_id_exists = Item.objects.get(id=item_id).exists()
            if is_item_id_exists:
                valid_item_ids.append(item_id)
        return valid_item_ids

    def get_form_details(self, form_id: int) -> \
        GetFormDto:
            form_obj = Form.objects.get(id=form_id)
            return GetFormDto(
                        form_id=form_obj.id,
                        form_name=form_obj.name,
                        form_state=form_obj.state,
                        form_description=form_obj.description,
                        closing_date=form_obj.closing_date
                    )

    def get_forms_section_dtos(self, form_id: int)-> \
        List[FormSectionDto]:
        form = Form.objects.filter(id=form_id) \
            .prefetch_related('section')
        sections = form.section_set.all()
        for section in sections:
            form_section_dtos.append(
                FormSectionDto(
                    form_id=form.id,
                    section_id
                    section_title: str
                    section_description: str
                )
            )

    def get_item_brands(self, item_ids: List[int])-> \
        List[ItemBrandsDto]:
            items = Item.objects.filter(id__in=item_ids) \
                            .prefetch_related('brand')
            item_brands_dtos = []
            for item in items:
                brand_ids = item.brand_set.all().values_list(['id'], flat=True)
                item_brands_dtos += \
                    self._convert_to_item_brand_dto(
                        item_id=item.id,
                        brand_ids=brand_ids
                    )
            return item_brands_dtos

    def _convert_to_item_brand_dto(self, item_id: int, brand_ids: List[int])-> \
        List[ItemBrandsDto]:
        dtos = []
        for brand_id in brand_ids:
            dtos.append(
                    ItemBrandsDto(
                        item_id=item_id,
                        brand_id=brand_id
                    )
                )
        return dtos

    def get_brand_details(self, brand_ids: List[int])-> \
        List[BrandDetailsDto]:
        pass

    def get_valid_section_ids(self, section_ids: List[int]):
        pass

    def get_section_item_dtos(self, section_ids: List[int])-> \
        List[SectionItemsDto]:
        pass

    def get_item_details(self, item_ids: List[int])-> \
        List[ItemDetailsDto]:
        pass
