from tkinter import ttk, constants
from repositories.travel_repository import Travel


class TravelListView:
    """Matkojen listauksesta vastaava näkymä"""

    def __init__(self, root, travels):
        """Luokan konstruktori. Luo uuden matkojen listausnäkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            travels:
                Lista Travel-olioita, jotka näytetään näkymässä     
        """
        self._root = root
        self._travels = travels
        self._frame = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_travels_list(self, travel):
        item_frame = ttk.Frame(master=self._frame)

        name_label = ttk.Label(master=item_frame, text=travel.name)
        name_label.grid(row=1, column=0, padx=(
            10, 5), pady=5, sticky=constants.W)

        participants_label = ttk.Label(
            master=item_frame, text=travel.participants)
        participants_label.grid(row=1, columnspan=3,
                                padx=5, pady=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, weight=1, minsize=50)
        item_frame.grid_columnconfigure(1, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize_no_saved_travels(self):
        item_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=item_frame, text="Ei tallennettuja matkoja")
        label.grid(row=1, column=1, padx=(10, 5), pady=5, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        if self._travels:
            for travel in self._travels:
                self._initialize_travels_list(travel)
        else:
            self._initialize_no_saved_travels()


class TravelView:
    def __init__(self, root, travel_service):
        self._root = root
        self._travel_service = travel_service
        self._frame = None
        self._travel_list_view = None
        self._travel_list_frame = None
        self._travels = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_travel_list(self):
        if self._travel_list_view:
            self._travel_list_view.destroy()

        travels = self._travel_service.get_users_travels()

        self._travel_list_view = TravelListView(
            self._travel_list_frame,
            travels
        )

        self._travel_list_view.pack()

    def _initialize_header(self):
        headline_label = ttk.Label(
            master=self._frame,
            text="Matkat"
        )
        headline_label.grid(row=0, column=0, padx=5, pady=5)

    def _initialize_title(self):
        title_label = ttk.Label(
            master=self._frame,
            text="Matkan nimi"
        )
        title_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)

        title2_label = ttk.Label(
            master=self._frame,
            text="Osallistujat"
        )
        title2_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.E)

    def _initialize_footer(self):
        create_travel_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi matka",
            command=self._handle_create_travel
        )

        create_travel_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
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

    def _handle_create_travel(self):
        travel_content = {
            "name": "Uusi matka",
            "participants": "Maisa"
        }
        travel = Travel(
            name=travel_content["name"], participants=travel_content["participants"])

        self._travel_service.create_travel(travel)
        self._initialize_travel_list()
