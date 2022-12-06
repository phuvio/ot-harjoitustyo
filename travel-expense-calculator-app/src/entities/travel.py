class Travel:
    """Luokka, joka kuvaa yksittäistä matkaa

    Attributes:
        name: Merkkijono, joka kuvaa matkan nimeä
        guide: Merkkijono, joka kuvaa matkan matkanjohtajaa
    """

    def __init__(self, name, guide):
        """Luokan konstruktori, joka luo uuden matkan

        Args:
            name: Merkkijono, joka kuvaa matkan nimeä
            guide: Merkkijono, joka kuvaa matkan matkanjohtajaa
        """

        self.name = name
        self.guide = guide
