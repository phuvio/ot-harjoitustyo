from tkinter import ttk, constants
from entities.payment import Payment
from services.payment_service import payment_service
from services.user_service import user_service
from services.travel_service import travel_service


class PaymentListView:
    """Maksujen listauksesta vastaava näkymä"""

    def __init__(self, root, payments):
        """Luokan konstruktori. Luo uuden maksujen listausnäkymän

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan
            payments:
                Lista Payment-olioita, jotka näytetään näkymässä
        """

        self._root = root
        self._payments = payments
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

        name_label = ttk.Label(master=item_frame, text=payment.receipt_name)
        name_label.grid(row=1, column=0, padx=(
            10, 5), pady=5, sticky=constants.W)

        amount_label = ttk.Label(master=item_frame, text=payment.amount)
        amount_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.W)

        payer_label = ttk.Label(master=item_frame, text=payment.payer)
        payer_label.grid(row=1, column=2, padx=5, pady=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, weight=1, minsize=50)
        item_frame.grid_columnconfigure(1, weight=1)
        item_frame.grid_columnconfigure(2, weight=1)
        item_frame.pack(fill=constants.X)

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

    def __init__(self, root, handle_logout, handle_show_create_payment_view, handle_show_travels_view):
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
        """

        self._root = root
        self._handle_logout = handle_logout
        self._handle_show_create_payment_view = handle_show_create_payment_view
        self._handle_show_travels_view = handle_show_travels_view
        self._user = user_service.get_current_user().username
        self._travel = travel_service.get_current_travel().name
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
        if self._payment_list_view:
            self._payment_list_view.destroy()

        payments = payment_service.get_payments_by_travel_and_action(
            self._travel, "maksu")

        self._payment_list_view = PaymentListView(
            self._payment_list_frame,
            payments
        )

        self._payment_list_view.pack()

    def _initialize_header(self):
        """Alustaa Maksut-näkymän headerin"""

        headline_label = ttk.Label(
            master=self._frame,
            text=f"Matkan {self._travel} maksut"
        )
        print(self._travel)
        headline_label.grid(row=0, column=0, padx=5, pady=5)

        user_label = ttk.Label(
            master=self._frame, text=f"Käyttäjä {self._user} kirjautuneena")
        user_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

        logout_button = ttk.Button(
            master=self._frame, text="Uloskirjautuminen", command=self._handle_logout)
        logout_button.grid(row=0, column=2, padx=5,
                           pady=5, sticky=constants.EW)

    def _initialize_title(self):
        """Alustaa Maksut-näkymän väliotsikot"""

        title_label = ttk.Label(
            master=self._frame,
            text="Maksun nimi"
        )
        title_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)

        title2_label = ttk.Label(
            master=self._frame,
            text="Summa"
        )
        title2_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.E)

        title3_label = ttk.Label(
            master=self._frame,
            text="Maksaja"
        )
        title3_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.E)

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

        travels_view_button = ttk.Button(
            master=self._frame,
            text="Matkat",
            command=self._handle_show_travels_view
        )

        travels_view_button.grid(
            row=4,
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
