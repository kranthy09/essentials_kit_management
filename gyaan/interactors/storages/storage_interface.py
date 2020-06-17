from abc import ABC, abstractmethod
from typing import List, Dict


class StorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def validate_user_follows_domain(self, user_id: int,
                                     domain_id: int):
        pass