class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää, joka on samalla matkanjohtaja

    Attributes:
        username: Merkkijono, joka kuvaa käyttäjän nimeä
        password: Merkkijono, joka kuvaa käyttäjän salasanaa
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän, joka toimii samalla matkanjohtajana

        Args:
            username: Merkkijono, joka kuvaa käyttäjän nimeä
            password: Merkkijono, joka kuvaa käyttäjän salasanaa
        """

        self.username = username
        self.password = password
