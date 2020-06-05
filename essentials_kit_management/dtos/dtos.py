from dataclasses import dataclass
from typing import List


@dataclass
class PostItemDto:
    item_id: int
    brand_id: int
    selected_quantity: int

@dataclass
class PostSectionDto:
    section_id: int
    item_id: int

@dataclass
class OrderListDto:
    section_item_dtos: List[PostSectionDto]
    item_brand_dtos: List[PostItemDto]