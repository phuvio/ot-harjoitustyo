from tkinter import ttk, constants
from services.payment_service import payment_service
from services.user_service import user_service
from services.travel_service import travel_service


class PaymentListView:
    """Maksujen listauksesta vastaava näkymä"""

    def __init__(self, root, payments, handle_show_single_payment_view):
        """Luokan konstruktori. Luo uuden maksujen listausnäkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            payments:
                Lista Payment-olioita, jotka näytetään näkymässä
            handle_show_single_payment_view:
                Kutsuttava arvo jota kutsutaan kun näytetään valittu yksittäinen maksu
        """

        self._root = root
        self._payments = payments
        self._handle_show_single_payment_view = handle_show_single_payment_view
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _initialize_payments_list(self, payment):
        """Näyttää yhden maksun luettelosta

        Args:
            payments:
                Payment-olio, joka näytetään luettelossa
        """

        item_frame = ttk.Frame(master=self._frame)

        name_button = ttk.Button(
            master=item_frame,
            text=payment.receipt_name,
            command=lambda: self._payment_button_function(payment)
        )
        name_button.grid(row=1, column=0, padx=(
            10, 5), pady=5, sticky=constants.W)

        date_label = ttk.Label(master=item_frame, text=payment.date)
        date_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.W)

        amount_label = ttk.Label(master=item_frame, text=payment.amount)
        amount_label.grid(row=1, column=2, padx=5, pady=5, sticky=constants.W)

        payer_label = ttk.Label(master=item_frame, text=payment.payer)
        payer_label.grid(row=1, column=3, padx=5, pady=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, weight=1, minsize=50)
        item_frame.grid_columnconfigure(1, weight=1)
        item_frame.grid_columnconfigure(2, weight=1)
        item_frame.pack(fill=constants.X)

    def _payment_button_function(self, payment):
        """Maksun valinta -nappulan funktio, joka valitsee maksun 
        ja siirtyy yksittäinen maksu -näkymään

        Args:
            payment: Valittu maksu Payment-olion muodossa
        """

        payment_service._payment = payment

        self._handle_show_single_payment_view()

    def _initialize_no_saved_payments(self):
        """Näyttää tekstin Ei tallennettuja maksuja"""

        item_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=item_frame, text="Ei tallennettuja maksuja")
        label.grid(row=1, column=1, padx=(10, 5), pady=5, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        """Näyttää luettelon maksuista"""

        self._frame = ttk.Frame(master=self._root)

        if self._payments:
            for payment in self._payments:
                self._initialize_payments_list(payment)
        else:
            self._initialize_no_saved_payments()


class PaymentView:
    """Maksujen näyttämisestä vastaava näkymä"""

    def __init__(
        self,
        root,
        handle_logout,
        handle_show_create_payment_view,
        handle_show_travels_view,
        handle_show_single_payment_view,
        handle_show_summary_view
    ):
        """Maksujen listauksesta vastaava näkymä

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_logout:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu ulos
            handle_show_create_payment_view:
                Kutsuttava arvo, jota kutsutaan kun lisätään maksu
            handle_show_travels_view:
                Kutsuttava arvo, jota kutsutaan kun palataan Matkan-näkymään
            handle_show_single_payment_view:
                Kutsuttava arvo, jota kutsutaan kun valitaan yksittäinen maksu
                ja siirrytään yksittäinen maksu -näkymään
            handle_show_summary_view:
                Kutsuttava arvo, jota kutsutaan kun siirrytään Yhteenveto-näkymään
        """

        self._root = root
        self._handle_logout = handle_logout
        self._handle_show_create_payment_view = handle_show_create_payment_view
        self._handle_show_travels_view = handle_show_travels_view
        self._handle_show_single_payment_view = handle_show_single_payment_view
        self._handle_show_summary_view = handle_show_summary_view
        self._user = user_service.get_current_user().username
        self._travel = travel_service.get_current_travel()
        self._frame = None
        self._payment_list_view = None
        self._payment_list_frame = None
        self._payments = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _initialize_payment_list(self):
        """Alustaa maksuluettelon"""
        if self._payment_list_view:
            self._payment_list_view.destroy()

        payments = payment_service.get_payments_by_travel_and_action(
            self._travel.travel_id, "maksu")

        self._payment_list_view = PaymentListView(
            self._payment_list_frame,
            payments,
            self._handle_show_single_payment_view
        )

        self._payment_list_view.pack()

    def _initialize_header(self):
        """Alustaa Maksut-näkymän headerin"""

        headline_label = ttk.Label(
            master=self._frame,
            text=f"Matkan {self._travel.name} maksut"
        )

        headline_label.grid(row=0, column=0, padx=5, pady=5)

        user_label = ttk.Label(
            master=self._frame, text=f"{self._user} kirjautuneena")
        user_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)

        logout_button = ttk.Button(
            master=self._frame, text="Uloskirjautuminen", command=self._handle_logout)
        logout_button.grid(row=0, column=3, padx=5,
                           pady=5, sticky=constants.E)

    def _initialize_title(self):
        """Alustaa Maksut-näkymän väliotsikot"""

        title_name_label = ttk.Label(
            master=self._frame,
            text="Maksun nimi"
        )
        title_name_label.grid(row=1, column=0, padx=5,
                              pady=5, sticky=constants.W)

        title_date_label = ttk.Label(
            master=self._frame,
            text="Päivämäärä"
        )
        title_date_label.grid(row=1, column=1, padx=5,
                              pady=5, sticky=constants.W)

        title_amount_label = ttk.Label(
            master=self._frame,
            text="Summa"
        )
        title_amount_label.grid(row=1, column=2, padx=5,
                                pady=5, sticky=constants.W)

        title_payer_label = ttk.Label(
            master=self._frame,
            text="Maksaja"
        )
        title_payer_label.grid(row=1, column=3, padx=5,
                               pady=5, sticky=constants.E)

    def _initialize_footer(self):
        """Alustaa Maksut-näkymän footerin"""

        create_payment_button = ttk.Button(
            master=self._frame,
            text="Luo uusi maksu",
            command=self._handle_show_create_payment_view
        )

        create_payment_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        summary_view_button = ttk.Button(
            master=self._frame,
            text="Yhteenveto",
            command=self._handle_show_summary_view
        )

        summary_view_button.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        travels_view_button = ttk.Button(
            master=self._frame,
            text="Matkat",
            command=self._handle_show_travels_view
        )

        travels_view_button.grid(
            row=5,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        """Näyttää Maksut-näkymän"""

        self._frame = ttk.Frame(master=self._root)
        self._payment_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_title()
        self._initialize_payment_list()
        self._initialize_footer()

        self._payment_list_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky=constants.EW
        )
