from essentials_kit_management.exceptions.exceptions \
    import InvalidForm
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface
from essentials_kit_management.interactors.storages \
    .dtos import FormCompleteDetailsDto


class GetForm:

    def __init__(self, storage: StorageInterface):
        self.storage = storage
    # TODO : validate form_id _/
    # TODO : from form_id, get form_dto 
    # TODO : from form_id, get form_section_dtos
    # TODO : from form_id, get_section_ids
    # TODO : from section_ids, call GetSections interactor
    # TODO : make form_complete_details_dto and call to presenter

    def get_form_sections_wrapper(self, form_id: int, user_id: int,
                                    presenter: PresenterInterface):

        try:
            form_complete_details_dto \
                =self.get_form_sections(form_id=form_id,
                                        user_id=user_id,
                                        presenter=presenter)
        except InvalidForm:
            presenter.raise_exception_for_invalid_form_id()
        response \
            = presenter.get_form_response(form_complete_details_dto)
        return response

    def get_form_sections(self, form_id: int, user_id: int,
                            presenter: PresenterInterface):

        self.storage.validate_form_id(form_id=form_id)
        form_dto = self.storage.get_form_details(form_id=form_id)
        form_section_dtos \
            = self.storage.get_forms_sections_dtos(form_id=form_id)
        section_ids = [form_section_dto.section_id 
                        for form_section_dto in form_section_dtos]
        from essentials_kit_management.interactors.get_section_items \
            import GetSectionItems

        get_section_items_interactor = GetSectionItems(storage=self.storage)

        sections_complete_details_dto \
            = get_section_items_interactor.get_section_items(
                    section_ids=section_ids
                )
        form_complete_details_dto \
            = FormCompleteDetailsDto(
                    form_details=form_dto,
                    form_sections_details=form_section_dtos,
                    section_items=sections_complete_details_dto.section_items,
                    item_details=sections_complete_details_dto.item_details,
                    item_brands=sections_complete_details_dto.item_brands,
                    brands_details=sections_complete_details_dto.brands_details
                )
        return form_complete_details_dto