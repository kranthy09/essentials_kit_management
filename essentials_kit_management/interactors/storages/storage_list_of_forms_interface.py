from abc import ABC, abstractmethod
from essentials_kit_management.interactors.storages \
    .dtos import (FormDto,
                  GetFormDto,
                  UserItemDto,
                  ItemBrandDto,
                  UserBrandDto,
                  FormSectionDto,
                  SectionItemDto
          )
from typing import List, Dict


class StorageListOfFormsInterface(ABC):

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
