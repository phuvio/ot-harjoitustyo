from tkinter import ttk, StringVar, constants
from services.user_service import user_service, InvalidCredentialsError


class LoginView:
    """Käyttäjän kirjautumisesta vastaava näkymä"""

    def __init__(self, root, handle_login, handle_show_create_user_view):
        """Luokan konstruktori. Luo uuden kirjautumisnäkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_login:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu sisään
            handle_show_create_user_view:
                Kutsuttava arvo, jota kutsutaan kun siirrytään rekisteröitymisvaiheeseen
        """

        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
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

    def _login_handler(self):
        """Sisäänkirjautumisen käsittelijä"""
        
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Väärä käyttäjätunnus tai salasana")

    def _show_error(self, message):
        """Näyttää virheilmoituksen"""

        self._error_variable.set(message)
        self._error_label.grid(row=1, column=0)

    def _hide_error(self):
        """Poistaa virheilmoituksen näkyvistä"""

        self._error_label.grid_remove()

    def _initialize_username_field(self):
        """Alustaa kentän käyttäjätunnus"""

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        """Alustaa kentän salasana"""
        password_label = ttk.Label(master=self._frame, text=("Salasana"))

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_title(self):
        """Alustaa näkymän otsikon"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Kirjaudu sisään"
        )
        headline_label.grid(row=0, column=0, padx=5, pady=5)

    def _initialize_footer(self):
        """Alustaaa näkymän footerin"""

        login_button = ttk.Button(
            master=self._frame,
            text="Sisäänkirjaus",
            command=self._login_handler
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Lisää käyttäjä",
            command=self._handle_show_create_user_view
        )

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        """Alustaa Sisäänkirjautuminen-näkymän"""
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
        self._initialize_footer()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        self._hide_error()
