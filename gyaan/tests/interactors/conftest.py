import pytest
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainStatsDto,
            UserDetailsDto,
            DomainRequestDto,
            PostDto,
            TagDto,
            PostTagDto,
            PostTagDetails,
            PostReactionsCount,
            PostCommentsCount,
            CommentReactionsCount,
            CommentRepliesCount,
            CommentDto,
            PostCompleteDetails)
from gyaan.interactors.presenters.dtos \
    import DomainDetailsDto, DomainDetailsWithPosts

@pytest.fixture
def domain_dto():
    domain_dto \
        = DomainDto(
            domain_id=1,
            name="Django",
            description="Python framework"
        )
    return domain_dto

@pytest.fixture
def domain_stats_dto():
    domain_stats_dto \
        = DomainStatsDto(
            followers=600,
            posts=999,
            stars=450
          )
    return domain_stats_dto

@pytest.fixture
def domain_expert_dtos():
    domain_expert_dtos = [
        UserDetailsDto(
            user_id=2,
            name="skywalker",
            profile_pic_url="skywalker.com"
        ),
        UserDetailsDto(
            user_id=3,
            name="chipmunk",
            profile_pic_url="chipmunk.com"
        )
    ]
    return domain_expert_dtos

@pytest.fixture
def domain_requests_dtos():
    domain_requests_dtos = [
        DomainRequestDto(
            request_id=5,
            user_id=2
        ),
        DomainRequestDto(
            request_id=6,
            user_id=2
        )
    ]
    return domain_requests_dtos

@pytest.fixture
def requested_user_dtos():
    requested_user_dtos = [
        UserDetailsDto(
            user_id=5,
            name="kanakkk",
            profile_pic_url="kanakkk.com"
        ),
        UserDetailsDto(
            user_id=6,
            name="jasper",
            profile_pic_url="jasper.com"
        )
    ]
    return requested_user_dtos

@pytest.fixture
def domain_details_dto(domain_dto):
    domain_details_dto = \
        DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=domain_expert_dtos,
            join_requests=domain_requests_dtos,
            requested_users=requested_user_dtos,
            is_user_domain_expert=True,
            user_id=10
        )
    return domain_details_dto

@pytest.fixture
def mock_response():
    mock_response = {
        "domain_id": 1,
        "name": "Django",
        "description": "Python framework",
        "user_id": 10,
        "is_user_domain_expert": True,
        "stats": {
            "followers": 600,
            "posts": 999,
            "stars": 450
        },
        "domain_experts": [
                {
                    "user_id": 2,
                    "name": "skywalker",
                    "profile_pic_url": "skywalker.com"
                },
                {
                    "user_id": 3,
                    "name": "chipmunk",
                    "profile_pic_url": "chipmunk.com"
                }
            ],
        "join_requests": [
                {
                    "request_id": 5,
                    "user_id": 2
                },
                {
                    "request_id": 6,
                    "user_id": 2
                }
            ],
        "requested_users": [
            {
                "user_id":5,
                "name":"kanakkk",
                "profile_pic_url":"kanakkk.com"
            },
            {
                "user_id": 6,
                "name": "jasper",
                "profile_pic_url": "jasper.com"
            }
        ]
    }
    return mock_response

@pytest.fixture
def post_dtos():

    post_dtos = [
        PostDto(
            post_id=1,
            posted_by_id=5,
            post_title="ORM",
            posted_at="13-12-2019,00:00:1568140200.00",
            post_content="Django ORM"
        ),
        PostDto(
            post_id=2,
            posted_by_id=6,
            post_title="Python",
            posted_at="13-12-2019,00:00:1568140200.00",
            post_content="Python oops in django"
        )
        
    ]
    return post_dtos

@pytest.fixture
def post_tag_details():

    tags = [
        TagDto(
            tag_id=1,
            tag_name="Python"
        ),
        TagDto(
            tag_id=2,
            tag_name="Django"
        )
    ]

    post_tags = [
        PostTagDto(
            post_id=1,
            tag_id=1
            
        ),
        PostTagDto(
            post_id=1,
            tag_id=2
            
        ),
        PostTagDto(
            post_id=2,
            tag_id=1
            
        )
    ]

    post_tag_details = \
        PostTagDetails(
            tags=tags,
            posttag_ids=post_tags
        )
    return post_tag_details

@pytest.fixture
def post_reactions_count():

    post_reaction_count  = [
        PostReactionsCount(
            post_id=1,
            reactions_count=1
        ),
        PostReactionsCount(
            post_id=2,
            reactions_count=2
        )
    ]
    return post_reactions_count

@pytest.fixture
def post_comments_count():

    post_comments_count = [
        PostCommentsCount(
            post_id=1,
            comments_count=1
        ),
        PostCommentsCount(
            post_id=2,
            comments_count=2
        )
    ]
    return post_comments_count

@pytest.fixture
def comment_reactions_count():

    comment_reactions_count = [
        CommentReactionsCount(
            comment_id=1,
            reactions_count=2
        ),
        CommentReactionsCount(
            comment_id=2,
            reactions_count=3
        )
    ]
    return comment_reactions_count

@pytest.fixture
def comment_replies_count():

    comment_replies_count = [
        CommentRepliesCount(
            comment_id=1,
            replies_count=3
        ),
        CommentRepliesCount(
            comment_id=2,
            replies_count=3
        )
    ]
    return comment_replies_count

@pytest.fixture
def comment_dtos():

    comment_dtos = [
        CommentDto(
            comment_id=1,
            commented_by_id=2,
            commented_on=1,
            comment_content='comment_content',
            commented_at="13-12-2019,00:00:1568140200.00",
            approved_domain_expert=2
        ),
        CommentDto(
            comment_id=2,
            commented_by_id=5,
            commented_on=2,
            comment_content='comment_content',
            commented_at="13-12-2019,00:00:1568140200.00",
            approved_domain_expert=3
        )
    ]
    return comment_dtos

@pytest.fixture
def user_dtos():

    user_dtos = [
        UserDetailsDto(
            user_id=2,
            name="gali",
            profile_pic_url="gali.com"
        ),
        UserDetailsDto(
            user_id=5,
            name="rishi kumar",
            profile_pic_url="kumar.com"
        ),
        UserDetailsDto(
            user_id=8,
            name="kranthi",
            profile_pic_url="kranthi.com"
        )
    ]
    return user_dtos

@pytest.fixture
def post_complete_details(post_dtos, post_reactions_count, user_dtos,
                          post_comments_count, comment_reactions_count,
                          comment_replies_count, comment_dtos,
                          post_tag_details):

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

@pytest.fixture
def posts_mock_response():

    posts_mock_response = [
        {
            
            "post_id": 1,
            "content": "Django ORM",
            "title": "ORM",
            "date": "13-12-2019,00:00:1568140200.00",
            "posted_by": {
                "user_id": 5,
                "name": "kanakkk",
                "profile_pic_url": "kanakkk.com"
            },
            "domain": {
                "domain_id": 1,
                "name": "Django"
            },
            "comments_count": 1,
            "hearts_count":1,
            "comments":[
                {
                    "comment_id":1,
                    "comment_content": "comment_content",
                    "commented_by":{
                        "user_id": 2,
                        "name": "gali",
                        "profile_pic_url": "gali.com"
                    },
                    "commented_at": "13-12-2019,00:00:1568140200.00",
                    "approved_by":{
                        "user_id":3,
                        "name":"chipmunk",
                        "profile_pic_url":"chipmunk.com"
                    },
                    "replies_count":2,
                    "hearts_count":3,
                }
            ],
            "tags":[
                {
                    "tag_id":1,
                    "name": "Python"
                },
                {
                    "tag_id":2,
                    "name":"Django"
                }
            ]
        },
        {
            
            "post_id": 2,
            "content": "Python oops in django",
            "title": "Python",
            "date": "13-12-2019,00:00:1568140200.00",
            "posted_by": {
                "user_id": 6,
                "name": "jasper",
                "profile_pic_url": "jasper.com"
            },
            "domain": {
                "domain_id": 1,
                "name": "Django"
            },
            "comments_count": 2,
            "hearts_count":2,
            "comments":[
                {
                    "comment_id":2,
                    "comment_content": "comment_content",
                    "commented_by":{
                        "user_id": 5,
                        "name": "kanakkk",
                        "profile_pic_url": "kanakkk.com"
                    },
                    "commented_at": "13-12-2019,00:00:1568140200.00",
                    "approved_by":{
                        "user_id":3,
                        "name":"chipmunk",
                        "profile_pic_url":"chipmunk.com"
                    },
                    "replies_count":3,
                    "hearts_count":3,
                }
            ],
            "tags":[
                {
                    "tag_id":1,
                    "name": "Python"
                }
            ]
        }
    ]
    return posts_mock_response

@pytest.fixture
def domain_details_with_posts(domain_details_dto,
                              post_complete_details):

    domain_details_with_posts = \
        DomainDetailsWithPosts(
            domain_details=domain_details_dto,
            post_complete_details=post_complete_details
        )
    return domain_details_with_posts

@pytest.fixture
def domain_posts_mock_response():

    domain_posts_mock_response = \
        {
        "domain_id": 1,
        "name": "Django",
        "description": "Python framework",
        "user_id": 10,
        "is_user_domain_expert": True,
        "stats": {
            "followers": 600,
            "posts": 999,
            "stars": 450
        },
        "domain_experts": [
                {
                    "user_id": 2,
                    "name": "skywalker",
                    "profile_pic_url": "skywalker.com"
                },
                {
                    "user_id": 3,
                    "name": "chipmunk",
                    "profile_pic_url": "chipmunk.com"
                }
            ],
        "join_requests": [
                {
                    "request_id": 5,
                    "user_id": 2
                },
                {
                    "request_id": 6,
                    "user_id": 2
                }
            ],
        "requested_users": [
            {
                "user_id":5,
                "name":"kanakkk",
                "profile_pic_url":"kanakkk.com"
            },
            {
                "user_id": 6,
                "name": "jasper",
                "profile_pic_url": "jasper.com"
            }
        ],
        "posts": posts_mock_response
    }
    return domain_posts_mock_response