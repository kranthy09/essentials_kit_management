import pytest
from unittest.mock import create_autospec, patch, call
from django_swagger_utils.drf_server.exceptions \
    import BadRequest, NotFound
from gyaan.interactors.get_posts \
    import GetPosts
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_get_posts_with_duplicate_post_ids():

    # Arrange
    domain_id = 2
    user_id = 1
    post_ids = [1,3,4,3]
    unique_post_ids = [1,3,4]
    duplicates = [3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetPosts(storage=storage)

    presenter.raise_exception_for_duplicate_post_ids \
        .side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_posts_wrapper(
                        post_ids=post_ids,
                        presenter=presenter
                   )

    err = presenter.raise_exception_for_duplicate_post_ids \
        .call_args.kwargs['duplicates']
    assert err.duplicates == duplicates

def test_get_posts_for_invalid_post_ids():

    # Arrange
    domain_id = 2
    user_id = 1
    post_ids = [1,2,3,100]
    valid_post_ids=[1, 2, 3]
    invalid_post_ids = [100]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetPosts(storage=storage)

    storage.get_valid_post_ids.return_value = valid_post_ids
    presenter.raise_exception_for_invalid_post_ids \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_posts_wrapper(
            post_ids=post_ids,
            presenter=presenter
        )

    storage.get_valid_post_ids \
        .assert_called_once_with(post_ids=post_ids)
    err = presenter.raise_exception_for_invalid_post_ids \
        .call_args.kwargs['invalids']
    assert err.invalids == invalid_post_ids


def test_get_posts(post_dtos, post_reactions_count, user_dtos,
                   post_comments_count, comment_reactions_count,
                   comment_replies_count, comment_dtos,
                   post_complete_details, posts_mock_response,
                   post_tag_details):

    # Arrange
    post_ids = [post_dto.post_id for post_dto in post_dtos]
    first_call_comments = [1]
    second_call_comments = [2]
    comment_ids = [1, 2]
    valid_post_ids = [1, 2]
    user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
    user_ids += [comment_dto.commented_by_id \
                for comment_dto in comment_dtos]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetPosts(storage=storage)

    storage.get_valid_post_ids.return_value = valid_post_ids
    storage.get_post_details.return_value = post_dtos
    storage.get_post_tags.return_value = post_tag_details
    storage.get_post_reactions_count \
        .return_value = post_reactions_count
    storage.get_post_comments_count \
        .return_value = post_comments_count
    storage.get_latest_comments \
        .side_effect = [first_call_comments,
                        second_call_comments]
    storage.get_comment_reactions_count \
        .return_value = comment_reactions_count
    storage.get_comment_replies_count \
        .return_value = comment_replies_count
    storage.get_comments.return_value \
        = comment_dtos
    storage.get_user_details \
        .return_value = user_dtos
    presenter.get_posts_response \
        .return_value = posts_mock_response

    # Act
    response = interactor.get_posts_wrapper(
            post_ids=post_ids,
            presenter=presenter
        )

    # Assert
    storage.get_valid_post_ids \
        .assert_called_once_with(post_ids=post_ids)
    storage.get_post_details \
        .assert_called_once_with(post_ids=post_ids)
    storage.get_post_reactions_count \
        .assert_called_once_with(post_ids=post_ids)
    storage.get_post_comments_count \
        .assert_called_once_with(post_ids=post_ids)
    storage.get_latest_comments \
        .assert_has_calls([
            call(post_id=1, no_of_comments=2),
            call(post_id=2, no_of_comments=2)
         ])
    storage.get_comment_reactions_count \
        .assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_replies_count \
        .assert_called_once_with(comment_ids=comment_ids)
    storage.get_comments \
        .assert_called_once_with(comment_ids=comment_ids)
    storage.get_user_details \
        .assert_called_once_with(user_ids=user_ids)
    presenter.get_posts_response \
        .assert_called_once_with(
            post_complete_details=post_complete_details)
    assert response == posts_mock_response