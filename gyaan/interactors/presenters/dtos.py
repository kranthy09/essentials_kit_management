from dataclasses import dataclass
from typing import List
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainStatsDto,
            UserDetailsDto,
            DomainRequestDto,
            )


@dataclass
class DomainDetailsDto:
    domain: DomainDto
    domain_stats: DomainStatsDto
    domain_experts: List[UserDetailsDto]
    join_requests: List[DomainRequestDto]
    requested_users: List[UserDetailsDto]
    is_user_domain_expert: bool
    user_id: int