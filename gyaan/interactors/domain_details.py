from gyaan.exceptions.exceptions \
    import (InvalidDomainId,
            InvalidUserIdInDomain)
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface

class DomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage
    
    # TODO : validate, domain_id
    # TODO : validate, user is following the domain
    # TODO : get domain experts
    # TODO : get domain stats
    # TODO : get domain details
    # TODO : get domain join request users
    def get_domain_details_wrapper(self, user_id: int, domain_id: int, 
                                     presenter: PresenterInterface):
        try:
            self._get_domain_details(domain_id=domain_id,
                                     user_id=user_id)
        except InvalidDomainId:
            presenter.raise_exception_for_invalid_domain_id()
        except InvalidUserIdInDomain:
            presenter.raise_exception_for_invalid_user_in_domain()
    

    def _get_domain_details(self, user_id: int,
                            domain_id: int):
        self.storage.validate_domain_id(domain_id=domain_id)
        self \
            ._check_is_user_follows_domain(user_id=user_id,
                                             domain_id=domain_id)

    def _check_is_user_follows_domain(self, user_id: int,
                                      domain_id: int):
        is_user_not_following_domain \
            = not(self.storage \
                .validate_user_follows_domain(user_id=user_id,
                                              domain_id=domain_id))
        if is_user_not_following_domain:
            raise InvalidUserIdInDomain