from abc import ABC
from abc import abstractmethod
from gyaan.interactors.presenters.dtos \
    import DomainDetailsDto


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
