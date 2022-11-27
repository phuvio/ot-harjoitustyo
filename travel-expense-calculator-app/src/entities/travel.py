class Travel:
    def __init__(self, name, participants, travel_id=None):
        self.name = name
        self.participants = participants
        self._id = travel_id
