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


def test_get_domain_details_interactor_invalid_user_in_domain():

    # Arrange
    user_id = 2
    domain_id = 5

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsInteractor(
                    storage=storage
                 )
    storage.validate_domain_id.return_value = None
    storage.validate_user_follows_domain.return_value = False
    presenter.raise_exception_for_invalid_user_in_domain \
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
    storage.validate_user_follows_domain \
        .assert_called_once_with(user_id=user_id,
                                 domain_id=domain_id)
    presenter.raise_exception_for_invalid_user_in_domain \
        .assert_called_once()

def test_get_domain_details_interactor(
                domain_stats_dto, domain_expert_dtos, response,
                domain_dto, domain_requests_dtos, requested_user_dtos):

    # Arrange
    user_id = 3
    domain_id = 4
    domain_expert_ids = [domain_expert.user_id 
                        for domain_expert in domain_expert_dtos]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsInteractor(
                    storage=storage
                 )
    storage.validate_domain_id.return_value = None
    storage.validate_user_follows_domain.return_value = True
    storage.get_domain_stats.return_value = domain_stats_dto
    storage.get_domain_expert_ids.return_value = domain_expert_ids
    storage.get_user_details.return_value = domain_expert_dtos
    storage.check_is_user_domain_expert.return_value = True
    storage.get_domain_requests.return_value = domain_requests_dtos
    storage.get_user_details.return_value = requested_user_dtos
    
    

    # Act
    response = interactor.get_domain_details_wrapper(
                    user_id=user_id,
                    domain_id=domain_id,
                    presenter=presenter
                )

    storage.validate_domain_id \
        .assert_called_once_with(domain_id=domain_id)
    storage.validate_user_follows_domain \
        .assert_called_once_with(user_id=user_id,
                                 domain_id=domain_id)
    storage.get_domain_stats \
        .assert_called_once_with(domain_id=domain_id)
    storage.get_domain_expert_ids \
        .assert_called_once_with(domain_id=domain_id)
    storage.get_user_details \
        .assert_called_once_with(domain_expert_ids=domain_expert_ids)
    storage.check_is_user_domain_expert \
        .assert_called_once_with(user_id=user_id,
                                 domain_id=domain_id)
    storage.get_domain_requests \
        .assert_called_once_with(user_id=user_id,
                                     domain_id=domain_id)
    storage.get_user_details.return_value = requested_user_dtos