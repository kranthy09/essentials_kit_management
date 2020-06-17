import pytest
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainStatsDto,
            UserDetailsDto,
            DomainRequestDto)


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