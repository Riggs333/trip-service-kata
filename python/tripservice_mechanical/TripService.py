from tripservice_mechanical.TripDAO import TripDAO
from tripservice_mechanical.UserNotLoggedInException import UserNotLoggedInException
from tripservice_mechanical.UserSession import UserSession


class TripService:
    def get_trips_by_user(self, user):
        logged_user = self.logged_in_user()
        is_friend = False
        trip_list = []
        if logged_user:
            for friend in user.get_friends():
                if friend is logged_user:
                    is_friend = True
                    break
            if is_friend:
                trip_list = TripDAO.find_trips_by_user(user)
            return trip_list
        else:
            raise UserNotLoggedInException()

    def logged_in_user(self):
        return UserSession.get_instance().get_logged_user()
