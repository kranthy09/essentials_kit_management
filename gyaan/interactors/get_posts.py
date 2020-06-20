from typing import List
from gyaan.exceptions.exceptions \
    import (UniquePostIdException,
            InvalidPostIdException)
from gyaan.interactors.storages.dtos \
    import (PostCompleteDetails,
            PostTagDetails)
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetPosts:

    def __init__(self, storage: StorageInterface):
        self.storage = storage
    # TODO : validate, post_ids - 
    # TODO : validate, duplicate post ids
    # TODO : from post_ids, get posts_dtos
    # TODO : from post_ids, get post_tag_details - 
    # TODO : from post_ids, get comments_count for posts
    # TODO : from post_ids, get reactions_count for posts
    # TODO : from post_ids, get comment_ids
    # TODO : from comment_ids, get comments_count for comments
    # TODO : from comment_ids, get reactions_count for comments
    # TODO : from comment_ids, get comment_dtos
    # TODO : from post_dtos and comment_dtos, get user_ids
    # TODO : from user_ids, get user_dtos

    def get_posts_wrapper(self, post_ids: List[int],
                          presenter: PresenterInterface):
        try:
            return self._prepare_post_response(post_ids=post_ids,
                                        presenter=presenter)
        except UniquePostIdException as err:
            presenter.raise_exception_for_duplicate_post_ids(duplicates=err)
        except InvalidPostIdException as err:
            presenter.raise_exception_for_invalid_post_ids(invalids=err)

    def _prepare_post_response(self, post_ids: List[int],
                                presenter: PresenterInterface):
        post_complete_details = self.get_posts(post_ids=post_ids)
        print(post_complete_details)
        return presenter.get_posts_response(
                        post_complete_details=post_complete_details)

    def get_posts(self, post_ids: List[int]):
        self.is_unique_post_ids(post_ids=post_ids)
        self._validate_post_ids(post_ids=post_ids)
        post_dtos = self.storage.get_post_details(post_ids=post_ids)
        post_tag_details \
            = self.storage.get_post_tags(post_ids=post_ids)
        post_reactions_count \
            = self.storage \
                .get_post_reactions_count(post_ids=post_ids)
        post_comments_count \
            = self.storage \
                .get_post_comments_count(post_ids=post_ids)
        comment_ids = self._get_latest_comments(post_ids=post_ids)
        comment_reactions_count \
            = self.storage \
                .get_comment_reactions_count(comment_ids=comment_ids)
        comment_replies_count \
            = self.storage \
                .get_comment_replies_count(comment_ids=comment_ids)
        comment_dtos \
            = self.storage \
                .get_comments(comment_ids=comment_ids)
        user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
        user_ids += [comment_dto.commented_by_id
                        for comment_dto in comment_dtos]
        user_dtos \
            = self.storage \
                .get_user_details(user_ids=user_ids)
        post_complete_details = \
            PostCompleteDetails(
                posts=post_dtos,
                post_tag_details=post_tag_details,
                post_comments_count=post_comments_count,
                post_reactions_count=post_reactions_count,
                comments=comment_dtos,
                comment_reactions_count=comment_reactions_count,
                comment_replies_count=comment_replies_count,
                users=user_dtos,
                tags=post_tag_details.tags,
                post_tags=post_tag_details.posttag_ids
            )
        return post_complete_details


    def is_unique_post_ids(self,
                           post_ids: List[int]):
        from collections import Counter
        duplicates = []
        cnt = Counter(post_ids)
        for key in cnt.keys():
            if cnt[key] > 1:
                duplicates.append(key)
        if duplicates:
            raise UniquePostIdException(
                            duplicates=duplicates)

    def _validate_post_ids(self, post_ids: int):
        valid_post_ids \
            = self.storage.get_valid_post_ids(post_ids=post_ids)
        invalid_post_ids = [
                post_id for post_id in post_ids \
                    if post_id not in valid_post_ids
            ]
        if invalid_post_ids:
            raise InvalidPostIdException(invalids=invalid_post_ids)

    def _get_latest_comments(self, post_ids: List[int]):
        comment_ids = []
        for post_id in post_ids:
            comment_ids \
                +=self.storage.get_latest_comments(post_id=post_id,
                                                  no_of_comments=2)
        return comment_ids
