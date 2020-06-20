# from gyaan.interactors.storages.dtos \
#     import (PostCompleteDetails,
#             CommentDto,
#             UserDetailsDto)
# from gyaan.interactors.presenters.dtos \
#     import DomainDetailsDto
# from gyaan.interactors.presenters.presenter_interface \
#     import PresenterInterface
# from typing import List, Dict


# class PresenterImplementation(PresenterInterface):

#     def get_create_post_response(self, post_id: int):
#         pass

#     def raise_invalid_post_id_exception(self):
#         pass

#     def get_create_comment_response(self, comment_id: int):
#         pass

#     def raise_exception_for_invalid_domain_id(self):
#         pass

#     def raise_exception_for_invalid_user_in_domain(self):
#         pass

#     def get_response_for_domain_details(self,
#                                 domain_details_dto: DomainDetailsDto
#                             ):
#         pass

#     def raise_exception_for_invalid_offset(self):
#         pass

#     def raise_exception_for_invalid_limit(self):
#         pass

#     def raise_exception_for_duplicate_post_ids(
#                                 self,
#                                 duplicates: List[int]):
#         pass

#     def raise_exception_for_invalid_post_ids(
#             self, invalids: List[int]
#         ):
#         pass

#     def get_posts_response(self, post_complete_details: PostCompleteDetails):
#         post_dtos = post_complete_details.posts
#         comment_dtos = post_complete_details.comment_dtos
#         user_dtos = post_complete_details.user_dtos
#         post_comments_count = post_complete_details.post_comments_count
#         post_hearts_count = post_complete_details.post_reactions_count
#         for post_dto in post_dtos:
#             user_id = post_dto.posted_by_id
#             post_comments \
#                 = self._get_post_comments(user_id, comment_dtos, user_dtos)
#             comments_count \
#                 = self._get_post_comments_count(
#                             post_id=post_dto.post_id,
#                             comment_content=post_comments_count.comments_count)
#             hearts_count \
#                 = self._get_hearts_count(
#                             post_id=post_dto.post_id,
#                             hearts_count=post_reactions_count.hearts_count)
    
    
    
#     def _get_post_comments(self, user_id: int,
#                           comment_dtos: List[CommentDto],
#                           user_dtos: List[UserDetailsDto]):

#         comments = []
#         for comment_dto in comment_dtos:
#             is_user_comment = user_id == comment_dto.commented_by_id
#             commented_by = self._get_user_info(user_id=user_id,
#                                           user_dtos=user_dtos)
#             if is_user_comment:
#                 comments.append(
#                     {
#                         "comment_id":comment_dto.comment_id,
#                         "comment_content":comment_dto.comment_content,
#                         "commented_by_id": commented_by
#                         "comment_reactions_count":
#                     }
#                 )
#     def _get_user_info(self, user_id: int,
#                       user_dtos: List[int])-> \
#         Dict[str, str]:
#         for user_dto in user_dtos:
#             is_user_dto = user_id == user_dto.user_id
#             if is_user_dto:
#                 user_info = {
#                     "user_id": user_dto.user_id,
#                     "name": user_dto.name,
#                     "profile_pic_url": user_dto.profile_pic_url
#                 }
#         return user_info