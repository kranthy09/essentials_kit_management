import pytest
from django_swagger_utils.drf_server.exceptions \
    import (BadRequest,
            NotFound)
from unittest.mock import create_autospec, patch
from gyaan.exceptions.exceptions \
    import InvalidDomainId
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.domain_with_posts \
    import DomainPostsInteractor
from gyaan.interactors.get_posts \
    import GetPosts


def test_get_domain_posts_with_invalid_offset():

    # Arrange
    user_id = 1
    domain_id = 2
    offset=-1
    limit=2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainPostsInteractor(
                    storage=storage
                 )
    presenter.raise_exception_for_invalid_offset.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
                        user_id=user_id, domain_id=domain_id,
                        offset=offset, limit=limit,
                        presenter=presenter
                   )
    presenter.raise_exception_for_invalid_offset.assert_called_once()

def test_get_domain_posts_with_invalid_limit():

    # Arrange
    user_id = 1
    domain_id = 2
    offset=1
    limit=-2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainPostsInteractor(
                    storage=storage
                 )
    presenter.raise_exception_for_invalid_limit.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
                        user_id=user_id, domain_id=domain_id,
                        offset=offset, limit=limit,
                        presenter=presenter
                   )
    presenter.raise_exception_for_invalid_limit.assert_called_once()

def test_get_domain_posts_with_invalid_domain_id():

    # Arrange
    user_id = 1
    domain_id = 200
    offset=1
    limit=2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainPostsInteractor(
                    storage=storage
                 )
    storage.validate_domain_id \
        .side_effect = InvalidDomainId
    presenter.raise_exception_for_invalid_domain_id \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_wrapper(
                        user_id=user_id, domain_id=domain_id,
                        offset=offset, limit=limit,
                        presenter=presenter
                   )
    storage.validate_domain_id \
        .assert_called_once_with(domain_id=domain_id)
    presenter.raise_exception_for_invalid_domain_id \
        .assert_called_once()

def test_get_domain_posts_with_user_not_follows_domain():

    # Arrange
    user_id = 1
    domain_id = 200
    offset=1
    limit=2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainPostsInteractor(
                    storage=storage
                 )
    storage.validate_domain_id \
        .return_value = None
    storage.validate_user_follows_domain.return_value = False
    presenter.raise_exception_for_invalid_user_in_domain \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_wrapper(
                        user_id=user_id, domain_id=domain_id,
                        offset=offset, limit=limit,
                        presenter=presenter
                   )
    storage.validate_domain_id \
        .assert_called_once_with(domain_id=domain_id)
    storage.validate_user_follows_domain \
        .assert_called_once_with(user_id=user_id,
                                 domain_id=domain_id)
    presenter.raise_exception_for_invalid_user_in_domain \
        .assert_called_once()

@patch.object(GetPosts, 'get_posts')
def test_get_domain_posts(get_posts_mock, post_complete_details):

    # Arrange
    user_id = 2
    domain_id = 1
    offset = 0
    limit = 2
    post_ids = [post_dto.post_id 
                for post_dto in post_complete_details.posts]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainPostsInteractor(
                    storage=storage
                 )

    storage.validate_domain_id \
        .return_value = None
    storage.validate_user_follows_domain.return_value = True
    storage.get_domain_post_ids.return_value = post_ids
    get_posts_mock.return_value = post_complete_details

    # Act
    result = interactor.get_domain_posts_wrapper(
                        user_id=user_id,
                        presenter=presenter,
                        domain_id=domain_id,
                        limit=limit,offset=offset
             )

    # Assert
    storage.validate_domain_id \
        .assert_called_once_with(domain_id=domain_id)
    storage.validate_user_follows_domain \
        .assert_called_once_with(user_id=user_id,
                                 domain_id=domain_id)
    storage.get_domain_post_ids \
        .assert_called_once_with(user_id=user_id, domain_id=domain_id,
                                 offset=offset, limit=limit)
    assert result == post_complete_details