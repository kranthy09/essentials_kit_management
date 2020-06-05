import datetime
from dataclasses import dataclass
from essentials_kit_management.constants.enums\
    import FormStateType
from typing import List


@dataclass
class FormDto:
    form_id: int
    form_name: str
    form_state: str
    delivery_date: datetime
    closing_date: datetime

@dataclass
class UserItemDto:
    form_id: int
    item_id: int
    user_id: int

@dataclass
class UserBrandDto:
    brand_id: int
    item_id: int
    max_quantity: int
    quantity: int
    price_per_item: int
    delivered_items: int
    is_closed: int

@dataclass
class FormMetricsDto:
    form_id: int
    item_id: int
    user_id: int
    total_items: int
    cost_incurred: int
    pending_items: int
    total_cost_estimate: int

@dataclass
class FormDetailsDto:
    form_id: int
    form_name: str
    total_items: int
    pending_items: int
    cost_incurred: int
    closing_date: datetime
    delivery_date: datetime
    total_cost_estimate: int
    form_state: FormStateType

@dataclass
class FormAllDetailsDto:
    total_forms_count: int
    form_details_dtos: List[FormDetailsDto]

@dataclass
class GetFormDto:
    form_id: int
    form_name: str
    form_state: FormStateType
    form_description: str
    closing_date: datetime

@dataclass
class FormSectionDto:
    form_id: int
    section_id: int
    section_title: str
    section_description: str

@dataclass
class SectionItemDto:
    section_id: int
    item_id: int
    item_name: str
    item_description: str

@dataclass
class ItemBrandDto:
    item_id: int
    brand_id: int
    brand_name: str
    min_quantity: int
    max_quantity: int
    price: int

@dataclass
class GetUserBrandDto:
    brand_id: int
    item_id: int
    brand_name: str
    max_quantity: int
    quantity: int
    price_per_item: int
    delivered_items: int
    is_closed: int

@dataclass
class SectionItemMetricsDto:
    item_id: int
    brand_id: int
    brand_selected: str
    estimated_cost: int
    quantity_selected: int

@dataclass
class FormDtoToPresenter:
    get_form_dto: GetFormDto
    form_section_dtos: List[FormSectionDto]
    section_item_dtos: List[SectionItemDto]
    item_brand_dtos: List[ItemBrandDto]
    section_item_metrics_dtos: List[SectionItemMetricsDto]
