from tkinter import ttk, StringVar, constants
from services.participant_service import participant_service
from services.user_service import user_service


class CreateParticipantView:
    """Matkustajan lisäämisestä vastaava näkymä"""

    def __init__(self, root, handle_create_participant, handle_cancel, handle_logout):
        """Luokan konstruktori. Luo uuden matkustajan lisääminen -näkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_create_participant:
                Kutsuttava arvo, jota kutsutaan kun matkustajaa luodaa.
                Saa argumenteikseen matkustajan nimen, matkan ja matkanjohtajan
            handle_cancel:
                Kutsuttava arvo, jota kutsutaan kun matkustajan lisääminen perutaan
            handle_logout:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu ulos
        """

        self._root = root
        self._handle_create_participant = handle_create_participant
        self._handle_cancel = handle_cancel
        self._handle_logout = handle_logout
        self._frame = None
        self._name_entry = None
        self._travel_entry = None
        self._guide = user_service.get_current_user().username
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _create_participant_handler(self):
        """Uuden matkustajan lisäyksen käsittelijä"""

        name = self._name_entry.get()
        travel = "*"
        guide = self._guide

        if len(name) == 0:
            self._show_error("Nimi on pakollinen")
            return

        participants_by_guide = participant_service.get_participants_by_guide(
            guide)

        for participant in participants_by_guide:
            if participant.name == name:
                self._show_error(f"Nimi {name} on jo olemassa")
                return

        if name == guide:
            self._show_error(f"Nimi {name} on jo olemassa")
            return

        participant_service.create_participant(name, travel, guide)
        self._handle_create_participant()

    def _show_error(self, message):
        """Näyttää virheilmoituksen"""

        self._error_variable.set(message)
        self._error_label.grid(row=1, column=2)

    def _hide_error(self):
        """Poistaa virheilmoituksen näkyvistä"""

        self._error_label.grid_remove()

    def _initialize_name_field(self):
        """Alustaa kentän Matkustajan nimi"""

        name_label = ttk.Label(master=self._frame, text="Matkustajan nimi")

        self._name_entry = ttk.Entry(master=self._frame)

        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._name_entry.grid(row=1, column=1, padx=5,
                              pady=5, sticky=constants.EW)

    def _initialize_title(self):
        """Alustaa näkymän otsikon"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Luo uusi matkustaja"
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
        """Näyttää uuden matkustajan luominen -näkymän"""

        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_title()
        self._initialize_name_field()

        create_participant_button = ttk.Button(
            master=self._frame,
            text="Luo uusi matkustaja",
            command=self._create_participant_handler
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._handle_cancel
        )

        self._frame.grid_columnconfigure(0, weight=1)

        create_participant_button.grid(
            row=3, column=1, padx=5, pady=5, sticky=constants.EW)
        cancel_button.grid(rowspan=4, columnspan=1, padx=5, pady=5, row=4,
                           column=1, sticky=constants.EW)

        self._hide_error()
