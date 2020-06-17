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

