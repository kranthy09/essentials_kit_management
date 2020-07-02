from essentials_kit_management.interactors.storages.dtos \
    import (FormDto,
            UserItemDto,
            UserBrandDto,
            ItemMetrics,
            FormMetricsDto
        )
from essentials_kit_management.interactors.storages \
    .storage_interface\
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
        item_metrics_dtos = self._get_item_metrics(user_brand_dtos)
        form_metrics_dtos = []
        for user_item_dto in user_item_dtos:
            for item_metrics_dto in item_metrics_dtos:
                if user_item_dto.item_id == item_metrics_dto.item_id:
                    form_metrics_dtos.append(
                        FormMetricsDto(
                            form_id=user_item_dto.form_id,
                            items = item_metrics_dto.item_count,
                            cost = item_metrics_dto.item_cost,
                            pendings = item_metrics_dto.item_pending,
                            order_cost = item_metrics_dto.item_order_cost
                        )
                    )
        return form_metrics_dtos


    def _get_item_metrics(
                    self,
                    user_brand_dtos: List[UserBrandDto]
                ):
        item_metrics_dtos = []
        for user_brand_dto in user_brand_dtos:
            item_count = user_brand_dto.quantity
            item_cost \
                = user_brand_dto.quantity \
                    *user_brand_dto.price_per_item
            if user_brand_dto.is_closed:
                item_pending = 0
            else:    
                item_pending \
                    = user_brand_dto.quantity \
                        - user_brand_dto.delivered_items
            item_order_cost \
                = user_brand_dto.delivered_items \
                    * user_brand_dto.price_per_item
            item_metrics_dtos.append(
                ItemMetrics(
                    item_id=user_brand_dto.item_id,
                    item_count=item_count,
                    item_cost=item_cost,
                    item_pending=item_pending,
                    item_order_cost=item_order_cost
                )
            )
        return item_metrics_dtos