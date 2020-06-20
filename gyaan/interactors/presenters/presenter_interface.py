from abc import ABC
from abc import abstractmethod
from gyaan.interactors.presenters.dtos \
    import DomainDetailsDto
from gyaan.interactors.storages.dtos \
    import PostCompleteDetails
from typing import List


class PresenterInterface(ABC):

    @abstractmethod
    def get_create_post_response(self, post_id: int):
        pass

    @abstractmethod
    def raise_invalid_post_id_exception(self):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_domain_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_in_domain(self):
        pass

    @abstractmethod
    def get_response_for_domain_details(self,
                                domain_details_dto: DomainDetailsDto
                            ):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit(self):
        pass

    @abstractmethod
    def raise_exception_for_duplicate_post_ids(
                                self,
                                duplicates: List[int]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_post_ids(
            self, invalids: List[int]
        ):
        pass

    @abstractmethod
    def get_posts_response(
                self, post_complete_details: PostCompleteDetails
            ):
        pass