from essentials_kit_management.constants.enums \
    import FormStateType
from essentials_kit_management.interactors.storages.dtos \
    import FormDto, FormMetricsDto
from essentials_kit_management.presenters \
    .presenter_implementation \
        import PresenterImplementation


def test_get_response_for_list_of_forms():
    # Arrange
    form_dtos = [
        FormDto(
            form_id=1,
            form_name="Snacks Form",
            form_state=FormStateType.LIVE.value,
            delivery_date="2020-12-12",
            closing_date="2020-12-14"
        ),
        FormDto(
            form_id=2,
            form_name="Fruits Form",
            form_state=FormStateType.DONE.value,
            delivery_date="2020-12-12",
            closing_date="2020-12-15"
        )
    ]
    
    form_metrics_dtos = [
        FormMetricsDto(
            form_id=1,
            items=30,
            order_cost=2000,
            pendings=20,
            cost=4000
        ),
        FormMetricsDto(
            form_id=2,
            items=50,
            order_cost=1000,
            pendings=15,
            cost=2000
        )
    ]
    presenter_response = [
        {
            "form_id": 1,
            "form_name":"Snacks Form",
            "closing_date":"2020-12-14",
            "next_delivery_date":"2020-12-12",
            "form_state":"Live",
            "total_items":30,
            "total_cost_estimate":4000,
            "pending_items":20,
            "cost_incurred":2000
        },
        {
            "form_id": 2,
            "form_name":"Fruits Form",
            "closing_date":"2020-12-15",
            "next_delivery_date":"2020-12-12",
            "form_state":"Done",
            "total_items":50,
            "total_cost_estimate":2000,
            "pending_items":15,
            "cost_incurred":1000
        }
    ]
    presenter = PresenterImplementation()
    # Act
    response = presenter.get_response_for_list_of_forms(
                    form_dtos=form_dtos,
                    form_metrics_dtos=form_metrics_dtos
              )

    # Assert
    assert response == presenter_response