from gyaan.interactors.r
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
        self._check_is_user_follows_domain(user_id=user_id,
                                           domain_id=domain_id)
        domain_dto = self.storage.get_domain_dto(domain_id=domain_id)
        domain_stats_dto = self.storage \
            .get_domain_stats(domain_id=domain_id)
        domain_expert_ids = self.storage \
            .get_domain_expert_ids(domain_id=domain_id)
        domain_experts_dtos = self.storage \
            .get_user_details(user_ids=domain_expert_ids)
        is_user_domain_expert, domain_requests, requested_user_dtos \
            = self._get_domain_expert_details(
                    user_id=user_id,
                    domain_id=domain_id
                  )
        domain_details_dto \
            = DomainDetailsDTO(
                domain=domain_dto,
                domain_stats_dto=domain_stats_dto,
                domain_experts_dtos=domain_experts_dtos,
                is_user_domain_expert=is_user_domain_expert,
                join_requests=domain_requests,
                requested_users=requested_user_dtos
            )

    def _check_is_user_follows_domain(self, user_id: int,
                                      domain_id: int):
        is_user_not_following_domain \
            = not(self.storage \
                .validate_user_follows_domain(user_id=user_id,
                                              domain_id=domain_id))
        if is_user_not_following_domain:
            raise InvalidUserIdInDomain

    def _get_domain_expert_details(self, user_id: int,
                                    domain_id: int):
        is_user_domain_expert = self.storage \
            .check_is_user_domain_expert(user_id=user_id,
                                         domain_id=domain_id)
        domain_requests_dtos = []
        requested_user_dtos = []
        if is_user_domain_expert:
            domain_requests_dtos = self.storage \
                .get_domain_requests(user_id=user_id,
                                     domain_id=domain_id)
        if domain_requests_dtos:
            requested_user_dtos = self.storage \
                .get_user_details(
                    user_id=[requested_user.request_id \
                        for requested_user in requested_user_dtos]
                 )
        return is_user_domain_expert, domain_requests_dtos, requested_user_dtos