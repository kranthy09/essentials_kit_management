from abc import ABC, abstractmethod
from typing import List, Dict
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainStatsDto,
            DomainRequestDto,
            UserDetailsDto)


class StorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def validate_user_follows_domain(self, user_id: int,
                                     domain_id: int):
        pass

    @abstractmethod

    @abstractmethod
    def get_domain_dto(self, domain_id: int)-> DomainDto:
        pass

    def get_domain_stats(self, domain_id: int)->DomainStatsDto:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int):
        pass

    @abstractmethod
    def get_user_details(self,
                user_ids: List[int])-> \
                List[UserDetailsDto]:
        pass

    @abstractmethod
    def check_is_user_domain_expert(self, user_id: int,
                                    domain_id: int)-> bool:
        pass

    @abstractmethod
    def get_domain_requests(self, user_id: int,
                            domain_id: int)-> \
                    List[DomainRequestDto]:
        pass
