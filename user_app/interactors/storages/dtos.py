from dataclasses import dataclass
from typing import List


@dataclass
class UserDto:
    user_id: int
    username: str

@dataclass
class UserDetailsDto:
    username: str
    password: str