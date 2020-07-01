import pytest
from user_app.interactors.storages.dtos \
    import UserDetailsDto


@pytest.fixture
def user():
    user = UserDetailsDto(
                username="Monty",
                password="monster@POGO123"
            )
    return user