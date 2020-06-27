from gyaan.exceptions.exceptions \
    import (InvalidOffset,
            InvalidLimit,
            InvalidDomainId,
            InvalidUserIdInDomain)
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface


class DomainPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_posts_wrapper(self, user_id: int, domain_id: int,
                                offset: int, limit: int,
                                presenter: PresenterInterface):

        try:
            return self.get_domain_posts(user_id=user_id, domain_id=domain_id,
                                    offset=offset, limit=limit)
        except InvalidOffset:
            presenter.raise_exception_for_invalid_offset()
        except InvalidLimit:
            presenter.raise_exception_for_invalid_limit()
        except InvalidDomainId:
            presenter.raise_exception_for_invalid_domain_id()
        except InvalidUserIdInDomain:
            presenter.raise_exception_for_invalid_user_in_domain()
    def get_domain_posts(self, user_id: int, domain_id: int,
                        offset: int, limit: int):
        self._check_offset_is_valid(offset=offset)
        self._check_limit_is_valid(limit=limit)
        self.storage.validate_domain_id(domain_id=domain_id)
        self._check_is_user_follows_domain(user_id=user_id,
                                           domain_id=domain_id)
        domain_post_details_dtos \
            = self.get_domain_posts_details(user_id=user_id,
                                            domain_id=domain_id,
                                            limit=limit, offset=offset)
        return domain_post_details_dtos

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

    def get_domain_posts_details(self, user_id:int, domain_id: int,
                                 limit: int, offset: int):

        post_ids \
            = self.storage.get_domain_post_ids(user_id=user_id,
                                            domain_id=domain_id,
                                            offset=offset, limit=limit)
        from gyaan.interactors.get_posts import GetPosts
        interactor_get_posts = GetPosts(
                        storage=self.storage
                     )
        post_details_dtos \
            = interactor_get_posts.get_posts(post_ids=post_ids)
        return post_details_dtos