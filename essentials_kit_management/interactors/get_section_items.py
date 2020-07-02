from typing import List
from essentials_kit_management.exceptions.exceptions \
    import UniqueSectionException, InvalidSectionId
from essentials_kit_management.interactors.storages \
    .dtos import SectionCompleteDetailsDto
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface

class GetSectionItems:

    def __init__(self, storage: StorageInterface):

        self.storage = storage
        # TODO : check is there are any duplicate section_ids
    	# TODO : validate section ids
    	# TODO : from section ids, get section_item_dtos
    	# TODO : from section_item_dtos, get item_ids
    	# TODO : from item_ids, get item_details_dtos
    	# TODO : call get_brands interactor with item_ids

    def get_section_items_wrapper(self, section_ids: List[int],
                                    presenter: PresenterInterface):

        try:
            sections_complete_details_dto \
                = self.get_section_items(section_ids=section_ids)
        except UniqueSectionException as err:
            presenter.raise_exception_for_duplicate_section_ids(duplicates=err)
        except InvalidSectionId as err:
            presenter.raise_exception_for_invalid_section_ids(invalids=err)
        return presenter \
                .get_section_items_response(sections_complete_details_dto)


    def get_section_items(self, section_ids: List[int]):

        self._check_is_sections_are_duplicates(section_ids=section_ids)
        self._check_is_sections_are_valid(section_ids=section_ids)
        section_items_dtos \
            = self.storage.get_section_items_dtos(section_ids=section_ids)
        item_ids = [section_item_dto.item_id 
                    for section_item_dto in section_items_dtos]
        item_details_dtos = self.storage.get_item_details(item_ids=item_ids)
        items_details_with_brands_dtos \
            = self.get_items_details_with_brands(item_ids=item_ids)
        sections_complete_details_dto = \
            SectionCompleteDetailsDto(
                section_items=section_items_dtos,
                item_details=item_details_dtos,
                item_brands=items_details_with_brands_dtos.item_brands,
                brands_details=items_details_with_brands_dtos.brand_details
            )
        return sections_complete_details_dto


    def _check_is_sections_are_duplicates(self, section_ids: List[int]):

        from collections import Counter
        duplicates = []
        cnt = Counter(section_ids)
        for key in cnt.keys():
            if cnt[key] > 1:
                duplicates.append(key)
        if duplicates:
            raise UniqueSectionException(duplicates=duplicates)

    def _check_is_sections_are_valid(self, section_ids: List[int]):

        valid_section_ids \
            = self.storage.get_valid_section_ids(section_ids=section_ids)
        invalids = [section_id for section_id in section_ids
                     if section_id not in valid_section_ids]
        if invalids:
            raise InvalidSectionId(invalids=invalids)

    def get_items_details_with_brands(self, item_ids: List[int]):

        from essentials_kit_management.interactors \
            .get_item_brands import GetBrands

        interactor_get_brands = GetBrands(storage=self.storage)

        items_details_with_brands_dtos \
            = interactor_get_brands.get_brands(item_ids=item_ids)
        return items_details_with_brands_dtos
