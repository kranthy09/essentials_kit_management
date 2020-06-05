from essentials_kit_management.interactors.storages.dtos \
    import (GetFormDto,
            ItemBrandDto,
            GetUserBrandDto,
            FormSectionDto,
            SectionItemDto,
            FormDtoToPresenter,
            SectionItemMetricsDto
    )
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface
from typing import List, Dict


class GetFormInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def get_form(self, user_id: int,
                    form_id: int
            )-> Dict[str, str]:
        get_form_dto = self.storage.get_form_dto(user_id, form_id)

        form_section_dtos = self.storage.get_form_section_dtos(form_id)

        section_ids = [form_section_dto.section_id for form_section_dto in form_section_dtos]
        section_item_dtos = self.storage.get_section_item_dtos(section_ids)

        item_ids = [section_item_dto.item_id for section_item_dto in section_item_dtos]
        item_brand_dtos =self.storage.get_item_brand_dtos(item_ids)

        get_user_brand_dtos = self.storage.get_user_brand_dtos(user_id, item_ids)

        section_item_metrics_dtos = self._get_section_item_metrics_dto(get_user_brand_dtos)

        form_dto_to_presenter\
            = self._get_convert_form_details_to_dto(
                    get_form_dto=get_form_dto,
                    form_section_dtos=form_section_dtos,
                    section_item_dtos=section_item_dtos,
                    item_brand_dtos=item_brand_dtos,
                    section_item_metrics_dtos=section_item_metrics_dtos
              )
        response = self.presenter.get_response_for_form(
                    form_dto_to_presenter=form_dto_to_presenter
                   )
        return response

    def _get_section_item_metrics_dto(self,
                                      get_user_brand_dtos: List[GetUserBrandDto]
                                     )-> List[SectionItemMetricsDto]:
        section_item_metric_dtos = []
        for get_user_brand_dto in get_user_brand_dtos:
            estimated_cost = get_user_brand_dto.quantity*get_user_brand_dto.price_per_item
            quantity_selected = get_user_brand_dto.quantity
            brand_selected = get_user_brand_dto.brand_name
            section_item_metric_dtos.append(
                        SectionItemMetricsDto(
                            item_id=get_user_brand_dto.item_id,
                            brand_id=get_user_brand_dto.brand_id,
                            brand_selected=brand_selected,
                            quantity_selected=quantity_selected,
                            estimated_cost=estimated_cost
                        )
                )
        return section_item_metric_dtos

    def _get_convert_form_details_to_dto(
                    self,
                    get_form_dto: GetFormDto,
                    form_section_dtos: List[FormSectionDto],
                    section_item_dtos: List[SectionItemDto],
                    item_brand_dtos: List[ItemBrandDto],
                    section_item_metrics_dtos: List[SectionItemMetricsDto]
              )-> FormDtoToPresenter:
        form_dto_to_presenter \
                = FormDtoToPresenter(
                    get_form_dto=get_form_dto,
                    form_section_dtos=form_section_dtos,
                    section_item_dtos=section_item_dtos,
                    item_brand_dtos=item_brand_dtos,
                    section_item_metrics_dtos=section_item_metrics_dtos
                  )
        return form_dto_to_presenter