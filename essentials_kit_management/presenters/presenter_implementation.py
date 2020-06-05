from essentials_kit_management.exceptions.exceptions\
    import InvalidUsername, InvalidPassword
from essentials_kit_management.interactors.presenters\
    .presenter_interface\
        import PresenterInterface
from common.dtos import UserAuthTokensDTO
from typing import List, Dict
from essentials_kit_management.interactors.storages.dtos\
    import FormDto, BrandDto, FormDetailsDto


class PresenterImplementation(PresenterInterface):

    def raise_invalid_username(self):
        raise InvalidUsername

    def raise_invalid_username_and_password(self):
        raise InvalidPassword

    def get_response_for_user_auth_token(self,
                                         user_tokens_dto: UserAuthTokensDTO
                                        ):
        response = {
            "user_id": user_tokens_dto.user_id,
            "access_token": user_tokens_dto.access_token,
            "refresh_token": user_tokens_dto.refresh_token,
            "expires_in": user_tokens_dto.expires_in
        }
        return response

    def get_response_for_list_of_forms(
                    self,
                    limit: int,
                    offset: int,
                    list_of_forms_details_dtos: List[FormDto]
        ):

        response = []
        for form_details_dto in list_of_forms_details_dtos:
            response.append(
                {
                    "form_id": form_details_dto.form_id,
                    "form_name": form_details_dto.form_name,
                    "form_state": form_details_dto.form_state,
                    "closing_date": form_details_dto.closing_date,
                    "expected_delivery_date": form_details_dto.expected_delivery_date,
                    "total_items": form_details_dto.total_items,
                    "total_cost_estimate": form_details_dto.total_cost_estimate,
                    "pending_items": form_details_dto.pending_items,
                    "cost_incurred": form_details_dto.cost_incurred
                }
            )
        return response