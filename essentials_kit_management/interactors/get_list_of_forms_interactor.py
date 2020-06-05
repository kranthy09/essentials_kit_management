from essentials_kit_management.interactors.storages.dtos \
    import (FormDto,
            UserBrandDto,
            UserItemDto,
            FormMetricsDto
        )
from essentials_kit_management.interactors.storages.storage_interface\
    import StorageInterface
from essentials_kit_management.interactors.presenters.presenter_interface\
    import PresenterInterface
from typing import List, Dict


class GetListOfFormsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def get_list_of_forms(self, user_id: int,
                          offset: int, limit: int
                         )-> List[Dict[str, str]]:
        form_dtos = self.storage.get_list_of_form_dtos(
                                        offset=offset,
                                        limit=limit
                                    )
        form_ids = [form_dto.form_id for form_dto in form_dtos]
        user_item_dtos = self.storage.get_user_item_dtos(
                                    user_id=user_id,
                                    form_ids=form_ids
                                )
        item_ids = [user_item_dto.item_id for user_item_dto in user_item_dtos]
        user_brand_dtos = self.storage.get_user_brand_dtos(
                                user_id=user_id,
                                item_ids=item_ids
                            )
        form_metrics_dtos \
            = self._get_form_metrics_dtos(user_item_dtos, user_brand_dtos)
        response \
            = self.presenter.get_response_for_list_of_forms(
                        form_dtos=form_dtos,
                        form_metrics_dtos=form_metrics_dtos
                )
        return response

    def _get_form_metrics_dtos(
                        self,
                        user_item_dtos: List[UserItemDto],
                        user_brand_dtos: List[UserBrandDto]
                    ):
        form_metrics_dtos = []
        for user_item_dto in user_item_dtos:
            total_items = 0
            pending_items = 0
            total_cost_estimate = 0
            cost_incurred = 0
            for user_brand_dto in user_brand_dtos:
                if user_item_dto.item_id == user_brand_dto.item_id:
                    total_items += user_brand_dto.quantity
                    total_cost_estimate \
                        += (user_brand_dto.quantity \
                                *user_brand_dto.price_per_item)
                    if user_brand_dto.is_closed:
                        pendings = 0
                    else:
                        pendings \
                            = (user_brand_dto.max_quantity \
                                    - user_brand_dto.delivered_items)
                    pending_items += pendings
                    cost_incurred \
                        += (user_brand_dto.delivered_items \
                                *user_brand_dto.price_per_item)
            form_metrics_dto = FormMetricsDto(
                                form_id=user_item_dto.form_id,
                                user_id=user_item_dto.user_id,
                                item_id=user_item_dto.item_id,
                                total_items=total_items,
                                total_cost_estimate=total_cost_estimate,
                                pending_items=pending_items,
                                cost_incurred=cost_incurred
                                )
            form_metrics_dtos \
                .append(form_metrics_dto)
        return form_metrics_dtos