# from unittest.mock import create_autospec
# from essentials_kit_management.interactors.storages.dtos \
#     import (GetFormDto,
#             ItemBrandDto,
#             GetUserBrandDto,
#             FormSectionDto,
#             SectionItemDto,
#             FormDtoToPresenter,
#             SectionItemMetricsDto
#     )
# from essentials_kit_management.constants.enums \
#     import FormStateType
# from essentials_kit_management.interactors.storages \
#     .storage_interface import StorageInterface
# from essentials_kit_management.interactors.presenters \
#     .presenter_interface import PresenterInterface
# from essentials_kit_management.interactors \
#     .get_form_interactor import GetFormInteractor


# def test_get_form_interactor():
#     # Arrange
#     user_id = 1
#     form_id = 1
#     form_dto = GetFormDto(
#                 form_id=1,
#                 form_name="Accom Form",
#                 form_state=FormStateType.LIVE.value,
#                 form_description="description",
#                 closing_date="2020-12-04"
#               )
#     form_section_dtos = [
#             FormSectionDto(
#                 form_id=1,
#                 section_id=1,
#                 section_title="Daily Products",
#                 section_description="description"
#             ),
#             FormSectionDto(
#                 form_id=1,
#                 section_id=2,
#                 section_title="Common Products",
#                 section_description="description"
#             )
#     ]
#     section_item_dtos = [
#         SectionItemDto(
#             section_id=1,
#             item_id=1,
#             item_name="item_name_1",
#             item_description="description"
#         ),
#         SectionItemDto(
#             section_id=2,
#             item_id=2,
#             item_name="item_name_2",
#             item_description="description"
#         )
#     ]
#     item_brand_dtos = [
#         ItemBrandDto(
#             item_id=1,
#             brand_id=1,
#             brand_name="brand_name_1",
#             min_quantity=0,
#             max_quantity=10,
#             price=50,
#         ),
#         ItemBrandDto(
#             item_id=2,
#             brand_id=2,
#             brand_name="brand_name_2",
#             min_quantity=0,
#             max_quantity=8,
#             price=80
#         )
#     ]
#     get_user_brand_dtos = [
#         GetUserBrandDto(
#             item_id=1,
#             brand_id=1,
#             brand_name="brand_name_1",
#             max_quantity=10,
#             quantity=8,
#             price_per_item=50,
#             delivered_items=5,
#             is_closed=False
#         ),
#         GetUserBrandDto(
#             item_id=2,
#             brand_id=2,
#             brand_name="brand_name_2",
#             max_quantity=20,
#             quantity=10,
#             price_per_item=30,
#             delivered_items=8,
#             is_closed=False
#         )
#         ]
#     section_item_metrics_dto \
#         = [
#             SectionItemMetricsDto(
#                 item_id=1,
#                 brand_id=1,
#                 brand_selected="brand_name_1",
#                 estimated_cost=400,
#                 quantity_selected=5
#             ),
#             SectionItemMetricsDto(
#                 item_id=2,
#                 brand_id=2,
#                 brand_selected="brand_name_2",
#                 estimated_cost=240,
#                 quantity_selected=8
#             )
#         ]

#     mock_response = {
#         "form_id": 1,
#         "form_name": "Accom Form",
#         "form_description": "description",
#         "form_state": FormStateType.LIVE.value,
#         "closing_date": "2020-12-04",
#         "sections_list": [
#                 {
#                     "section_id": 1,
#                     "section_title": "Daily Products",
#                     "section_description": "description",
#                     "items_list": [
#                             {
#                                 "item_id": 1,
#                                 "item_name": "item_name_1",
#                                 "item_description": "description",
#                                 "brands_available": [
#                                         {
#                                             "brand_id": 1,
#                                             "brand_name": "brand_name_1",
#                                             "min_quantity": 0,
#                                             "max_quantity": 10,
#                                             "price": 50
#                                         }
#                                     ]
#                             }
#                         ],
#                     "estimated_cost": 400,
#                     "quantity_selected": 5,
#                     "brand_selected": "brand_name_1"
#                 },
#                 {
#                     "section_id": 2,
#                     "section_title": "Common Products",
#                     "section_description": "description",
#                     "items_list": [
#                             {
#                                 "item_id": 2,
#                                 "item_name": "item_name_2",
#                                 "item_description": "description",
#                                 "brands_available": [
#                                         {
#                                             "brand_id": 2,
#                                             "brand_name": "brand_name_2",
#                                             "min_quantity": 0,
#                                             "max_quantity": 20,
#                                             "price": 30
#                                         }
#                                     ]
#                             }
#                         ],
#                     "estimated_cost": 240,
#                     "quantity_selected": 8,
#                     "brand_selected": "brand_name_2"
#                 }
#             ] 
#     }

#     storage = create_autospec(StorageInterface)
#     presenter = create_autospec(PresenterInterface)

#     interactor = GetFormInteractor(
#                     storage=storage,
#                     presenter=presenter
#                  )

#     storage.get_form_dto.return_value=form_dto
#     storage.get_form_section_dtos.return_value=form_section_dtos
#     storage.get_section_item_dtos.return_value=section_item_dtos
#     storage.get_item_brand_dtos.return_value=item_brand_dtos
#     storage.get_user_brand_dtos.return_value=get_user_brand_dtos
#     presenter.get_response_for_form.return_value=mock_response
#     # Act
#     response = interactor.get_form(
#                         user_id=user_id,
#                         form_id=form_id
#                 )

#     # Assert
#     storage.get_form_dto.assert_called_once()
#     storage.get_form_section_dtos.assert_called_once()
#     storage.get_section_item_dtos.assert_called_once()
#     storage.get_item_brand_dtos.assert_called_once()
#     storage.get_user_brand_dtos.assert_called_once()
#     presenter.get_response_for_form.assert_called_once()
#     assert response == mock_response
