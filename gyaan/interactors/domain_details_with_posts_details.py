from gyaan.exceptions.exceptions \
    import (InvalidOffset,
            InvalidLimit,
            InvalidDomainId,
            InvalidUserIdInDomain)
from gyaan.interactors.presenters.dtos \
    import DomainDetailsWithPosts
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface


class DomainDetailsWithPostsDetails:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_with_posts_wrapper(
                    self, user_id: int, domain_id: int,
                    limit: int, offset: int,
                    presenter: PresenterInterface):

        try:
            domain_details_with_posts = \
                self \
                    .get_domain_details_with_posts(
                                user_id=user_id,limit=limit,
                                offset=offset,domain_id=domain_id,
                                presenter=presenter)
        except InvalidOffset:
            presenter.raise_exception_for_invalid_offset()
        except InvalidLimit:
            presenter.raise_exception_for_invalid_limit()
        except InvalidDomainId:
            presenter.raise_exception_for_invalid_domain_id()
        except InvalidUserIdInDomain:
            presenter.raise_exception_for_invalid_user_in_domain()
        response = presenter \
            .get_domain_details_with_posts_response(
                    domain_details_with_posts=domain_details_with_posts)
        return response

    def get_domain_details_with_posts(
                    self, user_id: int, domain_id: int,
                    limit: int, offset: int,
                    presenter: PresenterInterface):

        self._check_offset_is_valid(offset=offset)
        self._check_limit_is_valid(limit=limit)
        self.storage.validate_domain_id(domain_id=domain_id)
        self._check_is_user_follows_domain(user_id=user_id,
                                           domain_id=domain_id)
        domain_details = self.get_domain_details(user_id=user_id,
                                domain_id=domain_id,
                                presenter=presenter)
        post_complete_details \
            = self.get_domain_with_posts(user_id=user_id,
                                         domain_id=domain_id,
                                         offset=offset, limit=limit,
                                         presenter=presenter)
        domain_details_with_posts = \
            DomainDetailsWithPosts(
                domain_details=domain_details,
                post_complete_details=post_complete_details
            )
        return domain_details_with_posts

    def _check_offset_is_valid(self, offset: int):
        if offset < 0:
            raise InvalidOffset

    def _check_limit_is_valid(self, limit: int):
        if limit < 0:
            raise InvalidLimit

    def _check_is_user_follows_domain(self, user_id: int,
                                      domain_id: int):
        is_user_not_following_domain \
            = not(self.storage \
                .validate_user_follows_domain(user_id=user_id,
                                              domain_id=domain_id))
        if is_user_not_following_domain:
            raise InvalidUserIdInDomain

    def get_domain_details(self, user_id: int, domain_id: int,
                            presenter: PresenterInterface):

        from gyaan.interactors.domain_details import DomainDetailsInteractor

        interactor_domain_details = DomainDetailsInteractor(
                                        storage=self.storage
                                    )
        domain_details_dto \
            = interactor_domain_details \
                .get_domain_details_wrapper(user_id=user_id,
                                            domain_id=domain_id,
                                            presenter=presenter)
        return domain_details_dto

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int,
                              presenter: PresenterInterface):

        from gyaan.interactors.domain_with_posts import DomainPostsInteractor

        interactor_domain_with_posts = DomainPostsInteractor(
                                            storage=self.storage
                                       )
        post_complete_details \
            = interactor_domain_with_posts \
                .get_domain_posts_wrapper(user_id=user_id,
                                          domain_id=domain_id,
                                          offset=offset,limit=limit,
                                          presenter=presenter)
        return post_complete_details
