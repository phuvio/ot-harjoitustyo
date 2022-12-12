from tkinter import ttk, constants
from entities.travel import Travel
from services.travel_service import travel_service
from services.user_service import user_service
from services.participant_service import participant_service


class TravelListView:
    """Matkojen listauksesta vastaava näkymä"""

    def __init__(self, root, travels, handle_show_payments_view):
        """Luokan konstruktori. Luo uuden matkojen listausnäkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            travels:
                Lista Travel-olioita, jotka näytetään näkymässä
            handle_show_payments_view:
                Kutsuttava arvo, jota kutsutaan kun näytetään matkan maksut
        """
        self._root = root
        self._travels = travels
        self._handle_show_payments_view = handle_show_payments_view
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _initialize_travels_list(self, travel):
        """Näyttää luettelon yhden matkan

        Args:
            travel:
                Travel-olio, joka näytetään luettelossa
        """
        item_frame = ttk.Frame(master=self._frame)

        name_button = ttk.Button(
            master=item_frame,
            text=travel.name,
            command=lambda: self._travel_button_function(travel)
        )

        name_button.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)

        participants = participant_service.get_participants_by_guide_and_travel(
            travel.guide, travel.travel_id)
        participants_names = []
        for participant in participants:
            participants_names.append(participant.name)

        participants_label = ttk.Label(
            master=item_frame, text=participants_names)
        participants_label.grid(row=1, columnspan=2,
                                padx=5, pady=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, weight=1, minsize=50)
        item_frame.grid_columnconfigure(1, weight=1)
        item_frame.pack(fill=constants.X)

    def _travel_button_function(self, travel):
        """Matkan valinta -nappulan funktio, joka valitsee matkan ja siirtyy maksut-näkymään

        Args:
            travel: Valittu matka Travel-olion muodossa
        """

        travel_service._travel = travel

        self._handle_show_payments_view()

    def _initialize_no_saved_travels(self):
        """Näyttää tekstin Ei tallennettuja matkoja"""

        item_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=item_frame, text="Ei tallennettuja matkoja")
        label.grid(row=1, column=1, padx=(10, 5), pady=5, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        """Näyttää luettelon matkoista"""

        self._frame = ttk.Frame(master=self._root)

        if self._travels:
            for travel in self._travels:
                self._initialize_travels_list(travel)
        else:
            self._initialize_no_saved_travels()


class TravelView:
    """Matkojen näyttämisestä vastaava näkymä"""

    def __init__(self, root, handle_logout, handle_show_create_travel_view, hadle_show_payments_view):
        """Matkojen listauksesta vastaava näkymä

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_logout:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu ulos
            handle_show_create_travel_view:
                Kutsuttava arvo, jota kutsutaan kun lisätään matka
            handle_show_payments_view:
                Kutsuttava arvo, jota kutsutaan kun katsotaan matkaan liittyvät maksut
        """
        self._root = root
        self._handle_logout = handle_logout
        self._handel_show_create_travel_view = handle_show_create_travel_view
        self._handle_show_payments_view = hadle_show_payments_view
        self._user = user_service.get_current_user()
        self._frame = None
        self._travel_list_view = None
        self._travel_list_frame = None
        self._travels = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _initialize_travel_list(self):
        """Alustaa matkaluettelon"""
        
        if self._travel_list_view:
            self._travel_list_view.destroy()

        travels = travel_service.get_users_travels(self._user.username)

        self._travel_list_view = TravelListView(
            self._travel_list_frame,
            travels,
            self._handle_show_payments_view
        )

        self._travel_list_view.pack()

    def _initialize_header(self):
        """Alustaa Matkat-näkymän headerin"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Matkat"
        )
        headline_label.grid(row=0, column=0, padx=5, pady=5)

        user_label = ttk.Label(
            master=self._frame, text=f"{self._user.username} kirjautuneena")
        user_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)

        logout_button = ttk.Button(
            master=self._frame, text="Uloskirjautuminen", command=self._handle_logout)
        logout_button.grid(row=0, column=3, padx=5,
                           pady=5, sticky=constants.E)

    def _initialize_title(self):
        """Alustaa Matkat-näkymän väliotsikot"""

        title_label = ttk.Label(
            master=self._frame,
            text="Matkan nimi"
        )
        title_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)

        title2_label = ttk.Label(
            master=self._frame,
            text="Matkustajat"
        )
        title2_label.grid(row=1, column=2, padx=5, pady=5, sticky=constants.E)

    def _initialize_footer(self):
        """Alustaa Matkat-näkymän footerin"""

        create_travel_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi matka",
            command=self._handel_show_create_travel_view
        )

        create_travel_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        """Näyttää Matkat-näkymän"""

        self._frame = ttk.Frame(master=self._root)
        self._travel_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_title()
        self._initialize_travel_list()
        self._initialize_footer()

        self._travel_list_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky=constants.EW
        )
