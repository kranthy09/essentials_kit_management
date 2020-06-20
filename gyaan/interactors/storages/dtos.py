import datetime
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class DomainStatsDto:
    followers: int
    posts: int
    stars: int

@dataclass
class UserDetailsDto:
    user_id: int
    name: str
    profile_pic_url: str

@dataclass
class DomainRequestDto:
    request_id: int
    user_id: int

@dataclass
class DomainDto:
    domain_id: int
    name: str
    description: str

@dataclass
class PostDto:
    post_id: int
    posted_by_id: int
    post_content: str
    post_title: str
    posted_at: datetime
    

@dataclass
class TagDto:
    tag_id: int
    tag_name: int

@dataclass
class PostTagDto:
    post_id: int
    tag_id: int

@dataclass
class PostTagDetails:
    tags: List[TagDto]
    posttag_ids: List[PostTagDto]

@dataclass
class PostCommentsCount:
    post_id: int
    comments_count: int

@dataclass
class PostReactionsCount:
    post_id: int
    reactions_count: int

@dataclass
class CommentDto:
    comment_id: int
    commented_on: int
    commented_by_id: int
    comment_content: str
    commented_at: datetime
    approved_domain_expert: int

@dataclass
class CommentRepliesCount:
    comment_id: int
    replies_count: int

@dataclass
class CommentReactionsCount:
    comment_id: int
    reactions_count: int

@dataclass
class PostCompleteDetails:
    posts: List[PostDto]
    post_tag_details: List[PostTagDetails]
    post_comments_count: List[PostCommentsCount]
    post_reactions_count: List[PostReactionsCount]
    comments: List[CommentDto]
    comment_reactions_count: List[CommentReactionsCount]
    comment_replies_count: List[CommentRepliesCount]
    users: List[UserDetailsDto]
    tags: List[TagDto]
    post_tags: List[PostTagDto]
