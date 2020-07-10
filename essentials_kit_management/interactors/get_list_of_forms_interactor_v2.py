from essentials_kit_management.interactors.storages \
    .dtos import UserSelectedBrandsDto, FormDetailsDto
from essentials_kit_management.exceptions.exceptions \
    import (InvalidOffSet,
            InvalidLimit)
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface
from typing import List


class GetListOfFormsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage
        # TODO : validate offset
        # TODO : validate limit
        # TODO : get all forms
        # TODO : get user filled forms
        # TODO : find out user not filled forms
        # TODO : make form_details_dto for user not filled forms
        # TODO : for user forms follow below steps
        # TODO : get total items
        # TODO : get pending items
        # TODO : get estimated cost
        # TODO : get cost incurred

    def get_list_of_forms_wrapper(self, user_id: int,
                                  limit: int, offset: int,
                                  presenter: PresenterInterface):

        try:
            form_details_dtos = self.get_list_of_forms(user_id=user_id,
                                   limit=limit,
                                   offset=offset)
        except InvalidOffSet:
            presenter.raise_exception_for_invalid_offset()
        except InvalidLimit:
            presenter.raise_exception_for_invalid_limit()

        response = presenter.get_response_for_form_details_dtos(form_details_dtos)
        return response

    def get_list_of_forms(self, user_id: int,
                          limit: int, offset: int):

        self._validate_offset(offset=offset)
        self._validate_limit(limit=limit)
        all_form_ids = self.storage.get_all_form_ids()
        user_form_ids = self.storage.get_user_form_ids(user_id=user_id)
        non_user_form_ids \
            = self._get_non_user_form_ids(all_form_ids, user_form_ids)
        non_user_form_dtos \
            = self.storage.get_non_user_form_dtos(form_ids=non_user_form_ids)
        form_details_dtos = self.get_form_details_dtos(
                                    user_form_ids=user_form_ids,
                                    user_id=user_id)

    def get_form_details_dtos(self, user_id: int,
                              user_form_ids: List[int])-> \
        List[FormDetailsDto]:

        form_details_dtos = []
        for form_id in user_form_ids:
            user_selected_brand_dtos = \
                self.storage.get_user_selected_brands(user_id=user_id, form_id=form_id)
            total_items = self._get_total_items(user_selected_brand_dtos)
            pending_items = self._get_pending_items(user_selected_brand_dtos)
            cost_estimate = self._get_cost_estimate(user_selected_brand_dtos)
            cost_incurred = self._get_cost_incurred(user_selected_brand_dtos)
            form_dto = self.storage.get_form_details(form_id=form_id)
            form_details_dtos.append(
                FormDetailsDto(
                    form_id=form_dto.form_id,
                    form_name=form_dto.form_name,
                    total_items=total_items,
                    pending_items=pending_items,
                    cost_incurred=cost_incurred,
                    closing_date=form_dto.closing_date,
                    delivery_date=form_dto.delivered_items,
                    total_cost_estimate=cost_estimate,
                    form_state=form_dto.form_state
                )
            )
        return form_details_dtos

    def _validate_offset(self, offset: int):
        if offset < 0:
            raise InvalidOffSet

    def _validate_limit(self, limit: int):
        if limit < 0:
            raise InvalidLimit

    def _get_non_user_form_ids(self,
                               all_form_ids: List[int],
                               user_form_ids: List[int])-> \
        List[int]:

        return [form_id for form_id in all_form_ids \
                if form_id not in user_form_ids]

    def _get_total_items(self, 
        user_selected_brand_dtos: List[UserSelectedBrandsDto])-> \
        int:

        total_items = 0
        for brand_dto in user_selected_brand_dtos:
            is_item_not_closed = not brand_dto.is_closed
            if is_item_not_closed:
                total_items += brand_dto.quantity
        return total_items

    def _get_pending_items(self,
        user_selected_brand_dtos: List[UserSelectedBrandsDto])-> \
        int:

        pending_items = 0
        for brand_dto in user_selected_brand_dtos:
            is_item_not_closed = not brand_dto.is_closed
            if is_item_not_closed:
                pending_items += brand_dto.quantity - brand_dto.delivered_items
        return pending_items

    def _get_cost_estimate(self,
        user_selected_brand_dtos: List[UserSelectedBrandsDto])-> \
        int:

        total_cost_estimate = 0
        for brand_dto in user_selected_brand_dtos:
            total_cost_estimate \
                += brand_dto.quantity * brand_dto.cost_per_item
        return total_cost_estimate

    def _get_cost_incurred(self,
        user_selected_brand_dtos: List[UserSelectedBrandsDto])-> \
        int:

        cost_incurred = 0
        for brand_dto in user_selected_brand_dtos:
            cost_incurred \
                += brand_dto.delivered_items * brand_dto.cost_per_item
        return cost_incurred