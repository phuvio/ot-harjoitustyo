from entities.travel import Travel
from repositories.travel_repository import (
    travel_repository as default_travel_repository)


class TravelService:
    def __init__(self, travel_repository=default_travel_repository):
        self._user = None
        self._travel_repository = travel_repository

    def create_travel(self, name, participants):
        travel = Travel(name, participants)

        return self._travel_repository.create(travel)

    def get_users_travels(self, username):

        travels = self._travel_repository.find_by_participant(username)

        if travels is None:
            return None
             
        return list(travels)

    def get_all_travels(self):

        return self._travel_repository.find_all()


travel_service = TravelService()
