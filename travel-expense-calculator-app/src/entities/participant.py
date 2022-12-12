import uuid


class Patricipant:
    """Luokka, joka kuvaa yksittäistä matkustajaa

    Attributes:
        name: Merkkijono, joka kuvaa matkustajan nimeä
        travel: Merkkijono, joka kuvaa matkaa, jolle matkustaja osallistuu
        guide: Merkkijono, joka kuvaa matkan, jolle matkustaja osallistuu, matkanjohtajaa
        participant_id: Kokonaisluku, joka kuvaa matkan id:tä
    """

    def __init__(self, name, travel, guide, participant_id=None):
        """Luokan konstruktori, joka luo uuden matkustajan

        Args:
            name: Merkkijono, joka kuvaa matkustajan nimeä
            travel: Merkkijono, joka kuvaa matkaa, jolle matkustaja osallistuu
            guide: Merkkijono, joka kuvaa matkan, jolle matkustaja osallistuu, matkanjohtajaa
            participant_id:
                Vapaaehtoinen, oletusarvoltaan None
                Kokonaisluku, joka kuvaa matkan id:tä
        """

        self.name = name
        self.travel = travel
        self.guide = guide
        self._participant_id = participant_id or str(uuid.uuid4())
