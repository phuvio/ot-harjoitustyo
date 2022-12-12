from tkinter import ttk, constants
from entities.payment import Payment
from services.payment_service import payment_service
from services.user_service import user_service
from services.travel_service import travel_service
from services.participant_service import participant_service


class SummaryListView:
    """Matkan maksujen yhteenvedon listauksesta vastaava näkymä"""

    def __init__(self, root, participants, payer_dic, buyer_dic):
        """Luokan konstruktori. Luo uuden matkan maksujen yhteenvedon
        listausnäkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            participants:
                Lista Participant-olioita, jotka näytetään näkymässä
            payer_dic:
                Dictionary matkustajista ja summa heidän maksamistaan maksuista
            buyer_dic:
                Dictionary matkustajista ja summa heidän ostoistaan
        """

        self._root = root
        self._participants = participants
        self._payer_dic = payer_dic
        self._buyer_dic = buyer_dic
        self._frame = None
        self._travel = travel_service.get_current_travel()

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _initialize_summary_list(self, participant):
        """Näyttää luettelon yhden matkustajan tiedot

        Args:
            participant:
                Participant-olio, joka näytetään luettelossa
        """

        item_frame = ttk.Frame(master=self._frame)

        participant_label = ttk.Label(
            master=item_frame,
            text=participant.name
        )
        participant_label.grid(row=2, column=0, padx=5,
                               pady=5, sticky=constants.W)

        payment_label = ttk.Label(
            master=item_frame,
            text=round(self._payer_dic[participant.name], 2)
        )
        payment_label.grid(row=2, column=1, padx=5, pady=5, sticky=constants.E)

        buying_label = ttk.Label(
            master=item_frame,
            text=round(self._buyer_dic[participant.name], 2)
        )
        buying_label.grid(row=2, column=2, padx=5, pady=5, sticky=constants.E)

        plus_minus_label = ttk.Label(
            master=item_frame,
            text=round(self._payer_dic[participant.name] -
                       self._buyer_dic[participant.name], 2)
        )
        plus_minus_label.grid(row=2, column=3, padx=5,
                              pady=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, weight=1, minsize=50)
        item_frame.grid_columnconfigure(1, weight=1, minsize=50)
        item_frame.grid_columnconfigure(2, weight=1, minsize=50)
        item_frame.grid_columnconfigure(3, weight=1, minsize=50)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        """Näyttää luettelon matkustajien yhteenvedoista"""

        self._frame = ttk.Frame(master=self._root)

        for participant in self._participants:
            self._initialize_summary_list(participant)


class SummaryView:
    """Matkan maksujen yhteenvedon näyttämisestä vastaava näkymä"""

    def __init__(self, root, handle_logout, handle_cancel):
        """Matkan maksujen yhteenvedon näyttämisestä vastaava näkymä

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_logout:
                 Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu ulos
            handle_cancel:
                Kutsuttava arvo, jota kutsutaan kun palataan maksut-näkymään
        """

        self._root = root
        self._handle_logout = handle_logout
        self._handle_cancel = handle_cancel
        self._frame = None
        self._guide = user_service.get_current_user().username
        self._travel = travel_service.get_current_travel()
        self._summary_list_view = None
        self._summary_list_frame = None
        self._participants = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _initialize_summary_list(self):
        """Alustaa luettelon yhden matkustajan tiedoista"""

        if self._summary_list_view:
            self._summary_list_view.destroy()

        payings = payment_service.get_payments_by_travel_and_action(
            self._travel.travel_id, "maksu")

        buyings = payment_service.get_payments_by_travel_and_action(
            self._travel.travel_id, "ostos")

        participants = participant_service.get_participants_by_guide_and_travel(
            self._travel.guide, self._travel.travel_id)

        payer_dic = {}
        buyer_dic = {}
        participants_names = []
        for participant in participants:
            participants_names.append(participant.name)
            payer_dic[participant.name] = 0.00
            buyer_dic[participant.name] = 0.00

        for pay in payings:
            payer_dic[pay.payer] += float(pay.amount)

        for buy in buyings:
            buyer_dic[buy.payer] += float(buy.amount)

        self._summary_list_view = SummaryListView(
            self._summary_list_frame,
            participants,
            payer_dic,
            buyer_dic
        )

        self._summary_list_view.pack()

    def _initialize_header(self):
        """Alustaa näkymän headerin"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Matkan " + self._travel.name + " yhteenveto"
        )
        headline_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        user_label = ttk.Label(
            master=self._frame,
            text=f"{self._guide} kirjautuneena"
        )
        user_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)

        logout_button = ttk.Button(
            master=self._frame,
            text="Uloskirjautuminen", command=self._handle_logout
        )
        logout_button.grid(row=0, column=3, padx=5,
                           pady=5, sticky=constants.E)

    def _initialize_title(self):
        """Alustaa näkymän otsikon"""

        participants_label = ttk.Label(
            master=self._frame,
            text="Matkustajat"
        )
        participants_label.grid(row=1, column=0, padx=5,
                                pady=5, sticky=constants.W)

        payings_label = ttk.Label(
            master=self._frame,
            text="Maksut yhteensä"
        )
        payings_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.E)

        buyings_label = ttk.Label(
            master=self._frame,
            text="Ostot yhteensä"
        )
        buyings_label.grid(row=1, column=2, padx=5, pady=5, sticky=constants.E)

        plus_minus_label = ttk.Label(
            master=self._frame,
            text="Plus/miinus"
        )
        plus_minus_label.grid(row=1, column=3, padx=5,
                              pady=5, sticky=constants.E)

    def _initialize(self):
        """Näyttää maksujen yhteenveto -näkymän"""

        self._frame = ttk.Frame(master=self._root)
        self._summary_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_title()
        self._initialize_summary_list()

        self._summary_list_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky=constants.EW
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text="Takaisin maksut-näkymään",
            command=self._handle_cancel
        )
        cancel_button.grid(row=5, column=2, padx=5,
                           pady=5, sticky=constants.EW)
