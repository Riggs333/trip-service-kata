from tripservice.exceptions import DependendClassCallDuringUnitTestException


class UserSession:

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return UserSession()

    def is_user_logged_in(self, user):
        raise DependendClassCallDuringUnitTestException(
            "UserSession.is_user_logged_in() should not be called in an unit test"
        )

    def get_logged_user(self):
        raise DependendClassCallDuringUnitTestException(
            "UserSession.get_logged_user() should not be called in an unit test"
        )
