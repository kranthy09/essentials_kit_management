from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from essentials_kit_management.interactors.storages\
    .dtos import (UserBrandDto,
                  FormDto,
                  UserBrandDto,
                  FormMetricsDto,
                  FormDtoToPresenter
          )
from typing import Dict, List


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_username(self):
        pass

    @abstractmethod
    def raise_invalid_username_and_password(self):
        pass

    @abstractmethod
    def get_response_for_user_auth_token(self,
                                         user_tokens_dto: UserAuthTokensDTO
                                        ):
        pass

    @abstractmethod
    def get_response_for_list_of_forms(
                    self,
                    form_dtos: List[FormDto],
                    form_metrics_dtos: List[FormMetricsDto]
            )-> List[Dict[str, str]]:
        pass

    @abstractmethod
    def get_response_for_form(
                    self,
                    form_dto_to_presenter: FormDtoToPresenter
                   )-> List[Dict[str,str]]:
        pass

    @abstractmethod
    def get_response_for_post_form(self)-> str:
        pass