from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from essentials_kit_management.interactors.storages\
    .dtos import (UserBrandDto,
                  FormDto,
                  UserBrandDto,
                  FormMetricsDto,
                  FormDtoToPresenter,
                  ItemDetailsWithBrandsDto,
                  SectionCompleteDetailsDto,
                  FormCompleteDetailsDto,
                  FormDetailsDto
          )
from typing import Dict, List


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_offset(self):
        pass

    @abstractmethod
    def get_response_for_list_of_forms(
                    self,
                    form_dtos: List[FormDto],
                    form_metrics_dtos: List[FormMetricsDto]
            )-> List[Dict[str, str]]:
        pass

    @abstractmethod
    def raise_exception_for_unique_item_expected(
                    self, duplicates: List[int]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_item_ids(
                    self, invalids: List[int]):
        pass

    @abstractmethod
    def get_brands_response(self, items_with_brands: ItemDetailsWithBrandsDto):
        pass

    @ abstractmethod
    def raise_exception_for_duplicate_section_ids(self, duplicates: List[int]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_section_ids(self, invalids: List[int]):
        pass

    @abstractmethod
    def get_section_items_response(self,
                sections_complete_details_dto: SectionCompleteDetailsDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_form_id(self):
        pass

    @abstractmethod
    def get_form_response(self, form_complete_details_dto: FormCompleteDetailsDto):
        pass

    @abstractmethod
    def get_response_for_form_details_dtos(self,
        form_details_dtos: List[FormDetailsDto]):
        pass