from essentials_kit_management.interactors.storages\
    .form_storage_interface\
        import FormStorageInterface
from essentials_kit_management.interactors.presenters\
    .form_presenter_interface\
        import FormPresenterInterface


class GetListofFormsInteractor:

    def __int__(self,
                form_storage: FormStorageInterface,
                form_presenter: FormPresenterInterface):
        self.form_storage = form_storage
        self.form_presenter = form_presenter