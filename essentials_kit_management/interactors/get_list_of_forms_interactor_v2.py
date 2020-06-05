from essentials_kit_management.interactors.storages\
    .dtos import (BrandDto,
                  FormDto,
                  FormDetailsDto
        )
from essentials_kit_management.interactors.storages\
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters\
    .presenter_interface import PresenterInterface
from typing import List


class GetListOfFormsInteractor:

    def __init__(self,
                 storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def get_list_of_forms(self,user_id: int, offset: int, limit: int):

        forms_all_details_dto\
            = self.storage.get_list_of_forms_dto(
                  user_id=user_id
              )
        list_of_forms_dto = forms_all_details_dto.forms_dto
        list_of_user_forms_dto = forms_all_details_dto.user_forms_dto
        list_of_user_brands_dto = forms_all_details_dto.brands_dto
        list_of_forms_details_dtos = []
        for user_form_dto in list_of_user_forms_dto:
            pending_items\
                = self._get_pending_items(
                    user_id=user_form_dto.user_id,
                    list_of_user_brands_dto=list_of_user_brands_dto
                  )
            total_cost_estimate\
                = self._get_total_cost_estimate(
                    user_id=user_form_dto.user_id,
                    list_of_user_brands_dto=list_of_user_brands_dto
                  )
            cost_incurred\
                = self._get_cost_incurred(
                    user_id=user_form_dto.user_id,
                    list_of_user_brands_dto=list_of_user_brands_dto
                  )
            total_items\
                = self._get_total_items(
                    user_id=user_form_dto.user_id,
                    list_of_user_brands_dto=list_of_user_brands_dto
                  )
            user_form_details_dto\
                = FormDetailsDto(
                        form_id=user_form_dto.form_id,
                        form_name=user_form_dto.form_name,
                        form_state=user_form_dto.form_state,
                        closing_date=user_form_dto.closing_date,
                        expected_delivery_date\
                            =user_form_dto.expected_delivery_date,
                        total_items=total_items,
                        total_cost_estimate=total_cost_estimate,
                        pending_items=pending_items,
                        cost_incurred=cost_incurred
                    )
            list_of_forms_details_dtos\
                .append(user_form_details_dto)
        for form_dto in list_of_forms_dto:
            form_details_dto \
                = FormDetailsDto(
                     form_id=user_form_dto.form_id,
                     form_name=user_form_dto.form_name,
                     form_state=user_form_dto.form_state,
                     closing_date=user_form_dto.closing_date,
                     expected_delivery_date\
                        =user_form_dto.expected_delivery_date,
                    total_items=0,
                    total_cost_estimate=0,
                    pending_items=0,
                    cost_incurred=0
                  )
            list_of_forms_details_dtos\
                .append(form_details_dto)
        response\
            = self.presenter.get_response_for_list_of_forms(
                    list_of_forms_details_dtos=list_of_forms_details_dtos,
                    limit=limit,
                    offset=offset
                )
        print(response)
        return response

    def _get_pending_items(
                self,
                user_id: int,
                list_of_user_brands_dto: List[BrandDto]
            ):
        pending_items = 0
        for brand_dto in list_of_user_brands_dto:

            is_user_id_contains = user_id == brand_dto.user_id
            if is_user_id_contains:
                is_item_brand_closed = brand_dto.is_closed
                if is_item_brand_closed:
                    pending_items = 0
                else:
                    pending_items\
                        += (brand_dto.max_quantity\
                            - brand_dto.delivered_items)
        return pending_items

    def _get_total_cost_estimate(
                self,
                user_id: int,
                list_of_user_brands_dto: List[BrandDto]
            ):
        total_cost_estimate = 0
        for brand_dto in list_of_user_brands_dto:
            is_user_id_contains = user_id == brand_dto.user_id
            if is_user_id_contains:
                total_cost_estimate\
                    += (brand_dto.quantity\
                        *brand_dto.price_per_item)
        return total_cost_estimate

    def _get_cost_incurred(
                self,
                user_id: int,
                list_of_user_brands_dto: List[BrandDto]
            ):
        cost_incurred = 0
        for brand_dto in list_of_user_brands_dto:

            is_user_id_contains = user_id == brand_dto.user_id
            if is_user_id_contains:
                cost_incurred\
                    += (brand_dto.delivered_items\
                        *brand_dto.price_per_item)
        return cost_incurred

    def _get_total_items(
                self,
                user_id: int,
                list_of_user_brands_dto: List[BrandDto]
            ):
        total_items = 0
        for brand_dto in list_of_user_brands_dto:
            is_user_id_contains = user_id == brand_dto.user_id
            if is_user_id_contains:
                total_items\
                    += brand_dto.quantity
        return total_items
