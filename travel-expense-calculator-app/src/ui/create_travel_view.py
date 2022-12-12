import tkinter as tk
from tkinter import ttk, StringVar, constants
from services.travel_service import travel_service
from services.participant_service import participant_service
from services.user_service import user_service


class CreateTravelView:
    """Matkan luomisesta vastaava näkymä"""

    def __init__(self, root, handle_create_travel, handle_cancel, handle_show_create_participant_view, handle_logout):
        """Luokan konstruktori. Luo uuden matkan luominen -näkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_create_travel:
                Kutsuttava arvo, jota kutsutaan kun matka luodaan.
                Saa argumenteikseen matkan nimen ja matkanjohtajan
            handle_cancel:
                Kutsuttava arvo, jota kutsutaan kun matkan lisääminen perutaan
            handle_show_create_participant_view:
                Kutsuttava arvo, jota kutsutaan kun lisätään matkustaja matkustajaluetteloon
            handle_logout:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu ulos
        """

        self._root = root
        self._handle_create_travel = handle_create_travel
        self._cancel = handle_cancel
        self._handel_show_create_participant_view = handle_show_create_participant_view
        self._handle_logout = handle_logout
        self._frame = None
        self._name_entry = None
        self._guide = user_service.get_current_user().username
        self._participants = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _create_travel_handler(self):
        """Uuden matkan lisäyksen käsittelijä"""

        name = self._name_entry.get()
        guide = self._guide
        participants_list = self._participants_selection.curselection()
        self._participants = [self._participants_selection.get(
            i) for i in participants_list]

        if len(name) == 0:
            self._show_error("Matkan nimi on pakollinen")
            return

        if self._participants == None or len(self._participants) == 0:
            self._show_error("Valitse matkustajat")
            return

        travel_by_name_and_guide = travel_service.get_travel_by_name_and_guide(
            name, guide)

        if travel_by_name_and_guide:
            self._show_error(f"Nimi {name} on jo olemassa")
            return

        try:
            travel_service.create_travel(name, guide)
            saved_travel = travel_service.get_travel_by_name_and_guide(
                name, guide)
            for participant in self._participants:
                participant_service.create_participant(
                    participant, saved_travel.travel_id, guide)
        except:
            self._show_error("Matkan tallentaminen epäonnistui")

        self._handle_create_travel()

    def _show_error(self, message):
        """Näyttää virheilmoituksen"""

        self._error_variable.set(message)
        self._error_label.grid(row=1, column=2)

    def _hide_error(self):
        """Poistaa virheilmoituksen näkyvistä"""

        self._error_label.grid_remove()

    def _initialize_name_field(self):
        """Alustaa kentän matkan nimi"""

        name_label = ttk.Label(master=self._frame, text="Matkan nimi")

        self._name_entry = ttk.Entry(master=self._frame)

        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._name_entry.grid(row=1, column=1, padx=5,
                              pady=5, sticky=constants.EW)

    def _initialize_participants_field(self):
        """Alustaa valintaruudun matkustajien valinta"""

        participant_label = ttk.Label(
            master=self._frame, text="Valitse matkustajat")

        participants_list = participant_service.get_participants_by_guide(
            self._guide)

        participants_set = set()
        for participant in participants_list:
            participants_set.add(participant.name)

        participants_set.add(self._guide)

        participants_list = tk.Variable(value=list(participants_set))

        self._participants_selection = tk.Listbox(
            master=self._frame,
            listvariable=participants_list,
            height=len(participants_set),
            selectmode=tk.MULTIPLE
        )

        participant_label.grid(row=2, column=0, padx=5,
                               pady=5, sticky=constants.W)
        self._participants_selection.grid(
            row=2, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_title(self):
        """Alustaa näkymän otsikon"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Luo uusi matka"
        )
        headline_label.grid(row=0, column=0, padx=5, pady=5)

        user_label = ttk.Label(
            master=self._frame,
            text=f"{self._guide} kirjautuneena"
        )
        user_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

        logout_button = ttk.Button(
            master=self._frame,
            text="Uloskirjautuminen", command=self._handle_logout
        )
        logout_button.grid(row=0, column=2, padx=5,
                           pady=5, sticky=constants.EW)

    def _initialize(self):
        """Näyttää uuden matkan luominen -näkymän"""

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
        self._initialize_participants_field()

        create_travel_button = ttk.Button(
            master=self._frame,
            text="Luo uusi matka",
            command=self._create_travel_handler
        )

        create_participant_button = ttk.Button(
            master=self._frame,
            text="Luo uusi matkustaja",
            command=self._handel_show_create_participant_view
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._cancel
        )

        self._frame.grid_columnconfigure(0, weight=1)

        create_travel_button.grid(
            row=3, column=1, padx=5, pady=5, sticky=constants.EW)
        create_participant_button.grid(
            row=4, column=1, padx=5, pady=5, sticky=constants.EW)
        cancel_button.grid(row=5, column=1, padx=5,
                           pady=5, sticky=constants.EW)

        self._hide_error()
