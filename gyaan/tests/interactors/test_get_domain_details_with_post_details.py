import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions \
    import BadRequest, NotFound
from gyaan.exceptions.exceptions \
    import InvalidDomainId, InvalidUserIdInDomain
from gyaan.interactors.domain_details_with_posts_details \
    import DomainDetailsWithPostsDetails
from gyaan.interactors.domain_with_posts \
    import DomainPostsInteractor
from gyaan.interactors.domain_details \
    import DomainDetailsInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_get_domain_details_with_posts_for_invalid_offset():

    # Arrange
    user_id = 1
    domain_id = 2
    offset = -1
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsWithPostsDetails(
                        storage=storage
                 )

    presenter.raise_exception_for_invalid_offset \
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_details_with_posts_wrapper(
                                user_id=user_id,
                                domain_id=domain_id,
                                offset=offset, limit=limit,
                                presenter=presenter)

    # Assert
    presenter.raise_exception_for_invalid_offset.assert_called_once()

def test_get_domain_details_with_posts_for_invalid_limit():

    # Arrange
    user_id = 1
    domain_id = 2
    offset = 1
    limit = -2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsWithPostsDetails(
                        storage=storage
                 )

    presenter.raise_exception_for_invalid_limit \
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_details_with_posts_wrapper(
                                user_id=user_id,
                                domain_id=domain_id,
                                offset=offset, limit=limit,
                                presenter=presenter)

    # Assert
    presenter.raise_exception_for_invalid_limit.assert_called_once()

def test_get_domain_details_with_posts_for_invalid_domain_id():

    # Arrange
    user_id = 100
    domain_id = 2
    offset = 1
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsWithPostsDetails(
                        storage=storage
                 )

    storage.validate_domain_id.side_effect = InvalidDomainId
    presenter.raise_exception_for_invalid_domain_id \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_details_with_posts_wrapper(
                                user_id=user_id,
                                domain_id=domain_id,
                                offset=offset, limit=limit,
                                presenter=presenter)

    # Assert
    presenter.raise_exception_for_invalid_domain_id.assert_called_once()

def test_get_domain_details_with_posts_for_invalid_user_in_domain():

    # Arrange
    user_id = 100
    domain_id = 2
    offset = 1
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsWithPostsDetails(
                        storage=storage
                 )

    storage.validate_domain_id.return_value = None
    storage.validate_user_follows_domain \
        .side_effect = InvalidUserIdInDomain
    presenter.raise_exception_for_invalid_user_in_domain \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_details_with_posts_wrapper(
                                user_id=user_id,
                                domain_id=domain_id,
                                offset=offset, limit=limit,
                                presenter=presenter)

    # Assert
    storage.validate_domain_id \
        .assert_called_once_with(domain_id=domain_id)
    storage.validate_user_follows_domain \
        .assert_called_once_with(
            user_id=user_id,
            domain_id=domain_id)
    presenter.raise_exception_for_invalid_user_in_domain \
        .assert_called_once()

@patch.object(DomainDetailsInteractor, 'get_domain_details_wrapper')
@patch.object(DomainPostsInteractor, 'get_domain_posts_wrapper')
def test_get_domain_details_with_posts(
                get_domain_details,get_domain_posts,
                domain_details_dto, post_complete_details,
                domain_details_with_posts,domain_posts_mock_response):

    # Arrange
    user_id = 1
    domain_id = 1
    offset = 0
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsWithPostsDetails(
                        storage=storage
                 )

    storage.validate_domain_id \
        .return_value = None
    storage.validate_user_follows_domain \
        .return_value = True
    get_domain_details.return_value = domain_details_dto
    get_domain_posts.return_value = post_complete_details
    presenter.get_domain_details_with_posts_response \
        .return_value = domain_posts_mock_response

    # Act
    response = interactor.get_domain_details_with_posts_wrapper(
                            user_id=user_id,
                            domain_id=domain_id,
                            offset=offset, limit=limit,
                            presenter=presenter)

    # Assert
    storage.validate_domain_id \
        .assert_called_once_with(domain_id=domain_id)
    storage.validate_user_follows_domain \
        .assert_called_once()
    assert response == domain_posts_mock_response