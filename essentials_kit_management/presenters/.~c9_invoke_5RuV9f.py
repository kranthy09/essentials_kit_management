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
            FormDetailsDto,
            ItemDetailsWithBrandsDto,
            SectionCompleteDetailsDto,
            UniqueItemException
            InvalidItem
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

    def raise_exception_for_unique_item_expected(
                    self, duplicates: List[int]):
        raise UniqueItemException

    def raise_exception_for_invalid_item_ids(
                    self, invalids: List[int]):
        raise InvalidItem

    def get_brands_response(self, items_with_brands: ItemDetailsWithBrandsDto):

        brand_dtos = items_with_brands.brand_details
        item_brands = items_with_brands.item_brands

        brands_response \
            = self._get_item_brands_dicts(brand_dtos=brand_dtos,
                                         item_brands=item_brands)
        return brands_response

    def _get_item_brands_dicts(self,item_brands: List[ItemBrandsDto],
                                 brand_dtos: List[BrandDetailsDtos]):

        item_brands_dicts = []
        for item_brand in item_brands:
            brands = []
            for brand_dto in brand_dtos:
                if item_brand.brand_id == brand_dto.brand_id:
                    brands.append(
                        {
                            "brand_id": brand_dto.brand_id,
                            "brand_name": brand_dto.name,
                            "min_quantity": brand_dto.min_quantity,
                            "max_quantity": brand_dto.max_quantity,
                            "price": brand_dto.price
                        }
                    )
            item_brands_dicts.append(
                {
                    "item_id": item_brand.item_id,
                    "brands": brands
                }
            )
        return item_brands_dicts

    def raise_exception_for_duplicate_section_ids(self, duplicates: List[int]):
        raise UniqueSectionException 

    def raise_exception_for_invalid_section_ids(self, invalids: List[int]):
        raise InvalidSectionId

    def get_section_items_response(self,
                sections_complete_details_dto: SectionCompleteDetailsDto):

        
        section_items = sections_complete_details_dto.section_items
        item_details = sections_complete_details_dto.item_details
        item_brands = sections_complete_details_dto.item_brands
        brands_details = sections_complete_details_dto.brands_details

        section_items_dicts \
            = self._get_section_items_dicts(
                            section_items=section_items,
                            item_details=item_details)

        item_brands_dicts \
            = self._get_item_brands_dicts(item_brands=item_brands,
                                     brand_dtos=brands_details)
        complete_section_details_dicts \
            = self._get_complete_section_details_dicts(
                    section_items_dicts = section_items_dicts,
                    item_brands_dicts = item_brands_dicts
                )
        return complete_section_details_dicts

    def _get_section_items_dicts(self, section_items: List[SectionItemsDto],
                                item_details: List[ItemDetailsDto]):

        for section_item in section_items:
            items = []
            for item_dto in item_details:
                if section_item.item_id == item_dto.item_id:
                    items.append(
                        {
                            "item_id": item_dto.item_id,
                            "item_name": item_dto.name,
                            "item_description": item_dto.description
                        }
                    )
            section_item_dicts.append(
                    "section_id": section_item.section_id,
                    "items": items
                )
        return section_item_dicts

    def _get_complete_section_details_dicts(self, section_item_dicts,
                                            item_brands_dicts):

        complete_section_details_dicts = []
        for section_item_dict in section_item_dicts:
            items = section_item_dicts['items']
            combined_items = []
            for item in items:
                for item_brand_dict in item_brand_dicts:
                    if item['item_id'] == item_brand_dict['item_id']:
                        item.update(item_brand_dict)
                        combined_items.append(item)
                        complete_section_details_dicts.append(
                            {
                                "section_id": section_item_dict['section_id'],
                                "items": combined_items
                            }
                        )
        return complete_section_details_dicts

    def raise_exception_for_invalid_form_id(self):
        pass

