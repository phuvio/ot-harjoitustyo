from tkinter import ttk, StringVar, constants
from services.payment_service import payment_service
from services.user_service import user_service
from services.travel_service import travel_service


class CreatePaymentView:
    """Maksun lisäämisestä vastaava näkymä"""

    def __init__(self, root, handle_create_payment, handle_cancel, handle_logout):
        """Luokan konstruktori. Luo uuden maksun lisääminen -näkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_create_payment:
                Kutsuttava arvo, jota kutsutaan kun maksua luodaa.
                Saa argumenteikseen 
                    matkan, johon maksu liittyy, nimen
                    maksun nimen
                    maksun päivämäärän
                    maksun summan
                    maksutapahtuman, joka on joko maksu tai ostos
                    maksajan nimen
                    maksun lisätiedot
            handle_cancel:
                Kutsuttava arvo, jota kutsutaan kun maksun lisääminen perutaan
            handle_logout:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu ulos
        """

        self._root = root
        self._handle_create_payment = handle_create_payment
        self._handle_cancel = handle_cancel
        self._handle_logout = handle_logout
        self._frame = None
        self._guide = user_service.get_current_user().username
        self._travel = travel_service.get_current_travel()
        self._receipt_name_entry = None
        self._date_entry = None
        self._amount_entry = None
        self._payer_entry = None
        self._buyers_entry = None
        self._information_entry = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _create_payment_handler(self):
        pass

    def _show_error(self, message):
        """Näyttää virheilmoituksen"""

        self._error_variable.set(message)
        self._error_label.grid(row=1, column=2)

    def _hide_error(self):
        """Poistaa virheilmoituksen näkyvistä"""

        self._error_label.grid_remove()

    def _initialize_title(self):
        """Alustaa näkymän otsikon"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Luo uusi maksu"
        )
        headline_label.grid(row=0, column=0, padx=5, pady=5)

        user_label = ttk.Label(
            master=self._frame,
            text=f"Kayttäjä {self._guide} kirjautuneena"
        )
        user_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

        logout_button = ttk.Button(
            master=self._frame,
            text="Uloskirjautuminen", command=self._handle_logout
        )
        logout_button.grid(row=0, column=2, padx=5,
                           pady=5, sticky=constants.EW)

    def _initialize(self):
        """Näyttää uuden maksun luominen -näkymän"""

        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_title()

        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._handle_cancel
        )

        self._frame.grid_columnconfigure(0, weight=1)

        cancel_button.grid(row=5, column=1, padx=5,
                           pady=5, sticky=constants.EW)

        self._hide_error()
