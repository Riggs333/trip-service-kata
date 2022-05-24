import unittest.mock as mock

import pytest

from tripservice.exceptions import UserNotLoggedInException
from tripservice.trip import Trip
from tripservice.trip_service import TripService
from tripservice.user import User


@pytest.fixture
def trip_service():
    return TripService()


@mock.patch("tripservice.trip_service.UserSession")
def test_should_throw_exception_when_user_not_logged_in(user_session_mock,
                                                        trip_service):
    user_session_mock.get_instance.return_value.get_logged_user.return_value = None
    with pytest.raises(UserNotLoggedInException):
        trip_service.get_trips_by_user(None)


@pytest.fixture
def logged_in_user():
    return User()


@mock.patch("tripservice.trip_service.UserSession")
def test_should_return_empty_list_when_user_has_no_friends(user_session_mock,
                                                           logged_in_user,
                                                           trip_service):
    user_session_mock.get_instance.return_value.get_logged_user.return_value = logged_in_user
    stranger = User()
    stranger.friends = []

    assert not trip_service.get_trips_by_user(stranger)


@mock.patch("tripservice.trip_service.UserSession")
def test_should_return_empty_list_when_user_has_other_friends(user_session_mock,
                                                              logged_in_user,
                                                              trip_service):
    user_session_mock.get_instance.return_value.get_logged_user.return_value = logged_in_user
    stranger = User()
    stranger.friends = [User()]

    assert not trip_service.get_trips_by_user(stranger)


@mock.patch("tripservice.trip_service.UserSession")
@mock.patch("tripservice.trip_service.TripDAO")
def test_get_trips_of_friends(trip_dao_mock, user_session_mock,
                              logged_in_user,
                              trip_service):
    user_session_mock.get_instance.return_value.get_logged_user.return_value = logged_in_user
    friend = User()
    friend.friends = [logged_in_user]
    trip = Trip()
    trip_dao_mock.find_trips_by_user.return_value = [trip]

    assert trip in trip_service.get_trips_by_user(friend)
