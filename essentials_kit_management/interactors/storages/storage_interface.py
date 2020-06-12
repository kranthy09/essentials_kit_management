from abc import ABC, abstractmethod
# from essentials_kit_management.interactors.storages\
#     .dtos import (FormDto,
#                   FormMetricsDto,
#                   FormDetailsDto)
from essentials_kit_management.interactors.storages\
    .dtos import (FormDto,
                  GetFormDto,
                  UserItemDto,
                  ItemBrandDto,
                  UserBrandDto,
                  FormSectionDto,
                  SectionItemDto
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
    def get_form_dto(self,
                     user_id: int,
                     form_id: int
                    )-> GetFormDto: 
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
    def get_form_section_dtos(
                    self,
                    form_id: int
            )-> List[FormSectionDto]:
        pass

    @abstractmethod
    def get_section_item_dtos(
                self,
                section_ids: List[int]
            )-> List[SectionItemDto]:
        pass

    @abstractmethod
    def get_item_brand_dtos(
                self,
                item_ids: List[int]
            )-> List[ItemBrandDto]:
        pass

    @abstractmethod
    def get_order(self, user_id: int,
                  item_id: int, brand_id: int
                )-> bool:
        pass

    @abstractmethod
    def update_order(self, user_id: int,
                     item_brand_dto: ItemBrandDto
                    ):
        pass

    @abstractmethod
    def create_order(self, user_id: int,
                     item_brand_dto: ItemBrandDto
                    ):
        pass