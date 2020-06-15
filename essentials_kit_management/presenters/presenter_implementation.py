from essentials_kit_management.exceptions.exceptions\
    import InvalidUsername, InvalidPassword
from essentials_kit_management.interactors.presenters\
    .presenter_interface\
        import PresenterInterface
from common.dtos import UserAuthTokensDTO
from typing import List, Dict
from essentials_kit_management.interactors.storages.dtos\
    import (FormDto,
            FormMetricsDto,
            FormDetailsDto
            
    )


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
                            form_dtos: List[FormDto],
                            form_metrics_dtos: List[FormMetricsDto]
                    )-> List[Dict[str, str]]:
        form_details = []
        for form_dto in form_dtos:
            total_items = 0
            total_cost_estimate = 0
            cost_incurred = 0
            pending_items = 0
            for form_metrics_dto in form_metrics_dtos:
                if form_dto.form_id == form_metrics_dto.form_id:
                    total_items += form_metrics_dto.items
                    total_cost_estimate += form_metrics_dto.cost
                    cost_incurred += form_metrics_dto.order_cost
                    pending_items += form_metrics_dto.pendings
            form_details.append(
                FormDetailsDto(
                    form_id=form_dto.form_id,
                    form_name=form_dto.form_name,
                    total_items=total_items,
                    pending_items=pending_items,
                    cost_incurred=cost_incurred,
                    closing_date=form_dto.closing_date,
                    delivery_date=form_dto.delivery_date,
                    total_cost_estimate=total_cost_estimate,
                    form_state=form_dto.form_state
                )
            )
        response = self._convert_dto_to_dict(form_details)
        return response

    def _convert_dto_to_dict(
                        self,
                        form_details: List[FormDetailsDto]
                    ):
        response = []
        for form_detail in form_details:
            response.append(
                {
                    "form_id":form_detail.form_id,
                    "form_name": form_detail.form_name,
                    "form_state": form_detail.form_state,
                    "closing_date": form_detail.closing_date,
                    "next_delivery_date": form_detail.delivery_date,
                    "total_items": form_detail.total_items,
                    "total_cost_estimate": form_detail.total_cost_estimate,
                    "pending_items": form_detail.pending_items,
                    "cost_incurred": form_detail.cost_incurred
                }
            )
        return response





"""
    form_id: int
    cost_estimate: int
    pendings: int
    cost_for_purchase: int
    items_count: int
"""