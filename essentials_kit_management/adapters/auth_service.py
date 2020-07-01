from typing import List


class AuthService:

    @property
    def interface(self):
        from user_app.interfaces.service_interface \
            import ServiceInterface
        service = ServiceInterface()
        return service

    def get_user_tokens_dto(self, username, password):
        tokens_dto = self.interface.get_tokens_dto(
                                    username=username,
                                    password=password)
        return tokens_dto
