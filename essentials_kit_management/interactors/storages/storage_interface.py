from abc import ABC, abstractmethod
from essentials_kit_management.interactors.storages \
    .dtos import (FormDto,
                  GetFormDto,
                  UserItemDto,
                  ItemBrandDto,
                  UserBrandDto,
                  FormSectionDto,
                  SectionItemDto,
                  ItemBrandsDto,
                  BrandDetailsDto,
                  SectionItemsDto,
                  ItemDetailsDto
          )
from typing import List, Dict


class StorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: int):
        pass

    @abstractmethod
    def validate_username_and_password(self,
                                       username: str,
                                       password: str
                                      ):
        pass

    @abstractmethod
    def get_list_of_form_dtos(self,
                              offset: int,
                              limit: int
                        )-> List[FormDto]:
        pass

    @abstractmethod
    def get_user_item_dtos(self,
                           user_id: int,
                           form_ids: List[int]
                    )-> List[UserItemDto]:
        pass
    @abstractmethod
    def get_user_brand_dtos(self,
                        user_id: int,
                        item_ids: List[int]
                        )-> List[UserBrandDto]:
        pass

    @abstractmethod
    def get_valid_item_ids(self, item_ids: List[int]):
        pass

    @abstractmethod
    def get_item_brands(self, item_ids: List[int])-> \
        List[ItemBrandsDto]:
        pass

    @abstractmethod
    def get_brand_details(self, brand_ids: List[int])-> \
        List[BrandDetailsDto]:
        pass

    @abstractmethod
    def get_valid_section_ids(self, section_ids: List[int]):
        pass

    @abstractmethod
    def get_section_items_dtos(self, section_ids: List[int])-> \
        List[SectionItemsDto]:
        pass

    @abstractmethod
    def get_item_details(self, item_ids: List[int])-> \
        List[ItemDetailsDto]:
        pass

    @abstractmethod
    def validate_form_id(self, form_id: int):
        pass

    @abstractmethod
    def get_form_details(self, form_id: int) -> \
        GetFormDto:
        pass

    @abstractmethod
    def get_forms_sections_dtos(self, form_id: int)-> \
        List[FormSectionDto]:
        pass
