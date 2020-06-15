import datetime
from typing import List
from dataclasses import dataclass


@dataclass
class ItemQuantity:
    item_id: int
    quantity: int

@dataclass
class OrderDto:
    meal_id: int
    date: datetime
    order_time: datetime
    items: List[ItemQuantity]
    order_deadline_time: datetime

