class Travel:
    """Luokka, joka kuvaa yksittäistä matkaa

    Attributes:
        name: Merkkijono, joka kuvaa matkan nimeä
        guide: Merkkijono, joka kuvaa matkan matkanjohtajaa
        travel_id: Kokonaisluku, joka kuvaa matkan id:tä
    """

    def __init__(self, name, guide, travel_id=None):
        """Luokan konstruktori, joka luo uuden matkan

        Args:
            name: Merkkijono, joka kuvaa matkan nimeä
            guide: Merkkijono, joka kuvaa matkan matkanjohtajaa
            travel_id: Kokonaisluku, joka kuvaa matkan id:tä
        """

        self.name = name
        self.guide = guide
        self.travel_id = travel_id
