from user_app.exceptions.exceptions \
    import InvalidUsername, InvalidPassword
from user_app.interactors.storages.dtos \
    import UserDto
from user_app.interactors.storages.storage_interface \
    import StorageInterface
from user_app.models.models import UserInfo
from typing import List


class StorageImplementation(StorageInterface):

    def validate_username(self, username: str):

        is_username_not_exists = not UserInfo.objects.filter(username=username).exists()
        if is_username_not_exists:
            raise InvalidUsername
        return True

    def validate_username_and_password(self, username: str, password: str)-> \
        int:
        user = UserInfo.objects.get(username=username)
        is_password_doesnot_match = not user.check_password(password)

        if is_password_doesnot_match:
            raise InvalidPassword

        return user.id

    def get_valid_user_ids(self, user_ids: List[int]):

        valid_user_ids = []
        for user_id in user_ids:
            is_user_id_exists = UserInfo.objects.filter(id=user_id).exists()
            if is_user_id_exists:
                valid_user_ids.append(user_id)
        return valid_user_ids

    def get_user_details(self, user_ids: int)-> \
        List[UserDto]:

        users = List(UserInfo.objects.filter(id__in=user_ids))
        user_dtos = []
        for user in users:
            user_dtos.append(
                UserDto(
                    user_id=user.id,
                    username=user.username
                )
            )
        return user_dtos