from abc import ABC, abstractmethod
from typing import List, Dict
from typing import List
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainStatsDto,
            DomainRequestDto,
            UserDetailsDto,
            PostDto,
            PostTagDetails,
            PostReactionsCount,
            PostCommentsCount,
            CommentReactionsCount,
            CommentRepliesCount,
            CommentDto)


class StorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def validate_user_follows_domain(self, user_id: int,
                                     domain_id: int):
        pass

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
    def get_domain_requests(
            self, user_id: int, domain_id: int)-> \
        List[DomainRequestDto]:
        pass

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int])-> \
        List[int]:
        pass

    @abstractmethod
    def get_post_details(
            self, post_ids: List[int])-> \
        List[PostDto]:
        pass

    @abstractmethod
    def get_post_tags(self, post_ids: List[int])-> \
        PostTagDetails:
        pass

    @abstractmethod
    def get_post_reactions_count(self, post_ids: List[int])-> \
        PostReactionsCount:
        pass

    @abstractmethod
    def get_post_comments_count(self, post_ids: List[int])-> \
        PostCommentsCount:
        pass

    @abstractmethod
    def get_latest_comments(self, post_id: int,
                           no_of_comments: int)-> \
        List[int]:
        pass

    @abstractmethod
    def get_comment_reactions_count(self ,comment_ids: List[int])-> \
        List[CommentReactionsCount]:
        pass

    @abstractmethod
    def get_comment_replies_count(self, comment_ids: List[int])-> \
        List[CommentRepliesCount]:
        pass

    @abstractmethod
    def get_comments(self, comment_ids: List[int])-> \
        List[CommentDto]:
        pass