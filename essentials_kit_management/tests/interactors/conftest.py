import pytest
from typing import List
from essentials_kit_management.interactors.storages.dtos \
    import (ItemBrandsDto, BrandDetailsDto,
            ItemDetailsWithBrandsDto,
            SectionItemsDto,
            ItemDetailsDto,
            SectionCompleteDetailsDto)


@pytest.fixture
def item_brands_dtos():

    item_brands_dtos = [
        ItemBrandsDto(
            item_id=1,
            brand_id=1
        ),
        ItemBrandsDto(
            item_id=1,
            brand_id=2
        ),
        ItemBrandsDto(
            item_id=2,
            brand_id=3
        ),
        ItemBrandsDto(
            item_id=2,
            brand_id=4
        )
    ]
    return item_brands_dtos

@pytest.fixture
def brand_details_dtos():

    brand_details_dtos = [
        BrandDetailsDto(
            brand_id=1,
            name="Nestle",
            min_quantity=0,
            max_quantity=10,
            price=60
        ),
        BrandDetailsDto(
            brand_id=2,
            name="Amul",
            min_quantity=0,
            max_quantity=10,
            price=30
        ),
        BrandDetailsDto(
            brand_id=3,
            name="godrej",
            min_quantity=0,
            max_quantity=8,
            price=90
        ),
        BrandDetailsDto(
            brand_id=4,
            name="Britannia",
            min_quantity=0,
            max_quantity=6,
            price=20
        )
    ]
    return brand_details_dtos

@pytest.fixture
def items_details_with_brands_dto(item_brands_dtos, brand_details_dtos):

    items_details_with_brands_dto = \
        ItemDetailsWithBrandsDto(
            item_brands=item_brands_dtos,
            brand_details=brand_details_dtos
        )
    return items_details_with_brands_dto

@pytest.fixture
def get_brands_mock_response():

    get_brands_mock_response = [
        {
            "item_id": 1,
            "brands": [
                {
                    "brand_id": 1,
                    "name": "Nestle",
                    "min_quantity": 0,
                    "max_quantity" :10,
                    "price": 60
                },
                {
                    "brand_id": 2,
                    "name": "Amul",
                    "min_quantity": 0,
                    "max_quantity": 10,
                    "price": 30
                }
            ]
        },
        {
            "item_id": 2,
            "brands": [
                {
                    "brand_id": 3,
                    "name": "godrej",
                    "min_quantity": 0,
                    "max_quantity" :8,
                    "price": 90
                },
                {
                    "brand_id": 4,
                    "name": "Britannia",
                    "min_quantity": 0,
                    "max_quantity": 6,
                    "price": 20
                }
            ]
        }
    ]
    return get_brands_mock_response

@pytest.fixture
def section_items_dtos():

    section_items_dtos = [
        SectionItemsDto(
            section_id=1,
            item_id=1
        ),
        SectionItemsDto(
            section_id=2,
            item_id=2
        )
    ]
    return section_items_dtos

@pytest.fixture
def item_details_dtos():

    item_details_dtos = [
        ItemDetailsDto(
            item_id=1,
            name="Milk Powder",
            description="lorem"
        ),
        ItemDetailsDto(
            item_id=2,
            name="Biscuists",
            description="lorem"
        )
    ]
    return item_details_dtos

@pytest.fixture
def sections_complete_details_dto(section_items_dtos,
                                  item_details_dtos,
                                  items_details_with_brands_dto):

    sections_complete_details_dto = \
        sections_complete_details_dto = \
            SectionCompleteDetailsDto(
                section_items=section_items_dtos,
                item_details=item_details_dtos,
                item_brands=items_details_with_brands_dto.item_brands,
                brands_details=items_details_with_brands_dto.brand_details
            )
    return sections_complete_details_dto

@pytest.fixture
def get_sections_mock_response():

    get_sections_mock_response = [
        {
            "section_id":1,
            "items":[
                {
                    "item_id":1,
                    "item_name":"Milk Powder",
                    "item_description":"lorems",
                    "brands": [
                        {
                            "brand_id": 1,
                            "name": "Nestle",
                            "min_quantity": 0,
                            "max_quantity" :10,
                            "price": 60
                        },
                        {
                            "brand_id": 2,
                            "name": "Amul",
                            "min_quantity": 0,
                            "max_quantity": 10,
                            "price": 30
                        }
                    ]
                }
            ],
        },
        {
            "section_id":2,
            "items":[
                {
                    "item_id":2,
                    "item_name":"Biscuists",
                    "item_description":"lorems",
                    "brands": [
                        {
                            "brand_id": 3,
                            "name": "godrej",
                            "min_quantity": 0,
                            "max_quantity" :8,
                            "price": 90
                        },
                        {
                            "brand_id": 4,
                            "name": "Britannia",
                            "min_quantity": 0,
                            "max_quantity": 6,
                            "price": 20
                        }
                    ]
                }
            ],
        }
    ]

    return get_sections_mock_response