from tkinter import ttk, constants
from entities.payment import Payment
from services.payment_service import payment_service
from services.user_service import user_service
from services.travel_service import travel_service


class SinglePaymentView:
    """Yksittäisen maksun näyttämisestä vastaava näkymä"""

    def __init__(self, root, handle_logout, handle_cancel):
        """Yksittäisen maksun tietojen näyttämisestä vastaava näkymä

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
        self._payment = payment_service.get_current_payment()

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _initialize_header(self):
        """Alustaa näkymän otsikon"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Matkan " + self._travel.name + " maksu"
        )
        headline_label.grid(row=0, column=0, padx=5, pady=5)

        user_label = ttk.Label(
            master=self._frame,
            text=f"{self._guide} kirjautuneena"
        )
        user_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)

        logout_button = ttk.Button(
            master=self._frame,
            text="Uloskirjautuminen", command=self._handle_logout
        )
        logout_button.grid(row=0, column=2, padx=5,
                           pady=5, sticky=constants.E)

    def _initialize_receipt_info(self):
        """Alustaa yksittäisen maksun tiedot"""

        payer = payment_service.get_payment_by_travel_and_name_and_action(
            self._travel.travel_id,
            self._payment.receipt_name,
            "maksu"
        )

        buyers = payment_service.get_payment_by_travel_and_name_and_action(
            self._travel.travel_id,
            self._payment.receipt_name,
            "ostos"
        )
        buyers_names = []
        for buyer in buyers:
            buyers_names.append(buyer.payer)

        receipt_name_title = ttk.Label(
            master=self._frame,
            text="Maksun nimi"
        )
        receipt_name_title.grid(row=2, column=0, padx=5,
                                pady=5, sticky=constants.W)

        date_title = ttk.Label(
            master=self._frame,
            text="Päivämäärä"
        )
        date_title.grid(row=2, column=1, padx=5, pady=5, sticky=constants.W)

        amount_title = ttk.Label(
            master=self._frame,
            text="Summa"
        )
        amount_title.grid(row=2, column=2, padx=5, pady=5, sticky=constants.W)

        payer_title = ttk.Label(
            master=self._frame,
            text="Maksaja"
        )
        payer_title.grid(row=2, column=3, padx=5, pady=5, sticky=constants.E)

        receipt_name_label = ttk.Label(
            master=self._frame,
            text=self._payment.receipt_name
        )
        receipt_name_label.grid(row=3, column=0, padx=5,
                                pady=5, sticky=constants.W)

        date_label = ttk.Label(
            master=self._frame,
            text=self._payment.date
        )
        date_label.grid(row=3, column=1, padx=5, pady=5, sticky=constants.W)

        amount_label = ttk.Label(
            master=self._frame,
            text=self._payment.amount
        )
        amount_label.grid(row=3, column=2, padx=5, pady=5, sticky=constants.W)

        payer_label = ttk.Label(
            master=self._frame,
            text=payer[0].payer
        )
        payer_label.grid(row=3, column=3, padx=5, pady=5, sticky=constants.E)

        buyers_title = ttk.Label(
            master=self._frame,
            text="Ostajat"
        )
        buyers_title.grid(row=4, column=0, padx=5,
                          pady=5, sticky=constants.W)

        info_title = ttk.Label(
            master=self._frame,
            text="Maksun lisätiedot"
        )
        info_title.grid(row=4, column=2, padx=5,
                        pady=5, sticky=constants.W)

        buyers_label = ttk.Label(
            master=self._frame,
            text=buyers_names
        )
        buyers_label.grid(row=5, column=0, padx=5,
                          pady=5, sticky=constants.W)

        info_label = ttk.Label(
            master=self._frame,
            text=self._payment.information
        )
        info_label.grid(row=5, column=2, padx=5,
                        pady=5, sticky=constants.W)

    def _initialize_footer(self):
        """Alustaa näkymän footerin"""

        cancel_button = ttk.Button(
            master=self._frame,
            text="Takaisin maksut-näymään",
            command=self._handle_cancel
        )
        cancel_button.grid(row=6, column=2, padx=5,
                           pady=5, sticky=constants.EW)

    def _initialize(self):
        """Näyttää yksittäinen maksu -näkymän
        """

        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_receipt_info()
        self._initialize_footer()
        