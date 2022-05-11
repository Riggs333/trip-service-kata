from tripservice_mechanical.DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException


class TripDAO:
    @staticmethod
    def find_trips_by_user(user):
        raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked on an unit test.")
