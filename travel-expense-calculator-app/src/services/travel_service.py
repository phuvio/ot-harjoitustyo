from entities.travel import Travel


class TravelService:
    def __init__(self, travel_repository):
        self._user = None
        self._travel_repository = travel_repository

    def create_travel(self, content):
        travel = Travel(name=content["name"],
                        participants=content["participants"])

        return self._travel_repository.create(travel)

    def get_users_travels(self):

        travels = self._travel_repository.find_all()

        return list(travels)