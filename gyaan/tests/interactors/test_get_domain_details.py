import pytest
from unittest.mock import create_autospec
from gyaan.exceptions.exceptions \
    import InvalidDomainId
from django_swagger_utils.drf_server.exceptions \
    import (NotFound,
            BadRequest)
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.domain_details \
    import DomainDetailsInteractor

def test_get_domain_details_interactor_invalid_domain_id():

    # Arrange
    user_id = 2
    domain_id = -1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsInteractor(
                        storage=storage
                 )

    storage.validate_domain_id.side_effect = InvalidDomainId
    presenter.raise_exception_for_invalid_domain_id \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_details_wrapper(
                user_id=user_id,
                domain_id=domain_id,
                presenter=presenter
            )
    storage.validate_domain_id \
        .assert_called_once_with(domain_id=domain_id)
    presenter.raise_exception_for_invalid_domain_id \
        .assert_called_once()
    