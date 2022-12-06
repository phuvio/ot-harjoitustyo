from tkinter import ttk, StringVar, constants
from services.user_service import user_service, UsernameExistsError


class CreateUserView:
    """Käyttäjän rekisteröitymisestä vastaava näkymä"""

    def __init__(self, root, handle_create_user, handle_show_login_view):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_create_user:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä luodaan.
                Saa argumenteikseen käyttäjätunnuksen ja salasanan
            handle_show_login_user:
                Kutsuttava arvo, jota kutsutaan kun siirrytään kirjautumisnäkymään
        """

        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _create_user_handler(self):
        """Uuden käyttäjän lisäyksen käsittelijä"""

        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Käyttäjätunnus ja salasanat ovat pakollisia")
            return

        try:
            user_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Käyttäjätunnus {username} on jo olemassa")

    def _show_error(self, message):
        """Näyttää virheilmoituksen"""

        self._error_variable.set(message)
        self._error_label.grid(row=1, column=0)

    def _hide_error(self):
        """Poistaa virheilmoituksen näkyvistä"""

        self._error_label.grid_remove()

    def _initialize_username_field(self):
        """Alustaa kentän Käyttäjätunnus"""

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        """Alustaa kentän salasana"""

        password_label = ttk.Label(master=self._frame, text="Salasana")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_title(self):
        """Alustaa näkymän otsikon"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Luo uusi käyttäjä"
        )
        headline_label.grid(row=0, column=0, padx=5, pady=5)

    def _initialize(self):
        """Näyttää uuden käyttäjän luominen -näkymän"""

        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_title()
        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Takaisin sisäänkirjautumissivulle",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, row=6, column=0, sticky=constants.EW)

        self._hide_error()
