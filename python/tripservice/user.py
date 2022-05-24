class User:

    def __init__(self):
        self.trips = []
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, user):
        self.friends.append(user)

    def add_trip(self, trip):
        self.trips.append(trip)

    def trips(self):
        return self.trips
