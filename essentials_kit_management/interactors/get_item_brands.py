from essentials_kit_management.interactors.storages.dtos \
    import ItemDetailsWithBrandsDto
from essentials_kit_management.exceptions.exceptions \
    import (UniqueItemException,
            InvalidItem)
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface
from typing import List


class GetBrands:

    def __init__(self, storage: StorageInterface):

        self.storage = storage
    # TODO : check duplicate item ids
    # TODO : validate item ids
    # TODO : from item ids, get item_brand_dtos
    # TODO : from item_brand_dtos, get brand_ids
    # TODO : from brand_ids, get brand_dtos

    def get_brands_wrapper(self, item_ids: List[int],
                            presenter: PresenterInterface):

        try:
            items_details_with_brands_dto \
                = self.get_brands(item_ids=item_ids)
        except UniqueItemException as err:
            presenter.raise_exception_for_unique_item_expected(duplicates=err)
        except InvalidItem as err:
            presenter.raise_exception_for_invalid_item_ids(invalids=err)
        response \
            = presenter.get_brands_response(items_details_with_brands_dto)
        return response


    def get_brands(self, item_ids: List[int]):

        self._check_is_items_are_unique(item_ids=item_ids)
        self._check_invalid_item_ids(item_ids=item_ids)
        item_brands_dtos \
            = self.storage.get_item_brands(item_ids=item_ids)
        brand_ids = [item_brand_dto.brand_id 
                    for item_brand_dto in item_brands_dtos]
        brand_details_dtos \
            = self.storage.get_brand_details(brand_ids=brand_ids)
        items_details_with_brands_dto = \
            ItemDetailsWithBrandsDto(
                item_brands=item_brands_dtos,
                brand_details=brand_details_dtos
            )
        return items_details_with_brands_dto

    def _check_is_items_are_unique(self, item_ids: List[int]):
        from collections import Counter
        duplicates = []
        cnt = Counter(item_ids)
        for key in cnt.keys():
            if cnt[key] > 1:
                duplicates.append(key)
        if duplicates:
            raise UniqueItemException(duplicates=duplicates)

    def _check_invalid_item_ids(self, item_ids: List[int]):

        valid_item_ids \
            = self.storage.get_valid_item_ids(item_ids=item_ids)
        invalid_item_ids = [item_id for item_id in item_ids
                            if item_id not in valid_item_ids]
        if invalid_item_ids:
            raise InvalidItem(invalids=invalid_item_ids)