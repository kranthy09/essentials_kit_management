from userapp.exceptions.exceptions \
    import InvalidUsername, InvalidPassword
from userapp.storages.dtos \
    import UserDto
from userapp.interactors.storages.storage_interface \
    import StorageInterface
from userapp.models.models import User
from typing import List


class StorageImplementation(StorageInterface):

    def validate_username(self, username: str):

        is_username_not_exists = not User.objects.filter(username=username).exists()
        if is_username_not_exists:
            raise InvalidUsername

    def validate_username_and_password(self, username: str, password: str):
        is_password_doesnot_match = not \
                User.objects.filter(username=username, password=password).exists()
        if is_password_doesnot_match:
            raise InvalidPassword

    def get_valid_user_ids(self, user_ids: List[int]):

        valid_user_ids = []
        for user_id in user_ids:
            is_user_id_exists = User.objects.filter(id=user_id).exists()
            if is_user_id_exists:
                valid_user_ids.append(user_id)
        return valid_user_ids

    def get_user_details(self, user_ids: List[int]):

        users = List(User.objects.filter(id__in=user_ids))
        user_dtos = []
        for user in users:
            user_dtos.append(
                UserDto(
                    user_id=user.id,
                    username=user.username
                )
            )
        return user_dtos