import tkinter as tk
from tkinter import ttk, StringVar, constants
from services.payment_service import payment_service
from services.user_service import user_service
from services.travel_service import travel_service
from services.participant_service import participant_service
from tkcalendar import DateEntry


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
        self._payer_selection = None
        self._buyers_selection = None
        self._information_entry = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self._frame.destroy()

    def _create_payment_handler(self):
        """Uuden matkun lisäyksen käsittelijä"""

        receipt_name = self._receipt_name_entry.get()
        amount = self._amount_entry.get()
        date = self._date_entry.get_date()
        payer_list = self._payer_selection.curselection()
        payer = [self._payer_selection.get(i) for i in payer_list]
        buyers_list = self._buyers_selection.curselection()
        buyers = [self._buyers_selection.get(i) for i in buyers_list]
        information = self._information_entry.get()

        if len(receipt_name) == 0:
            self._show_error("Maksun nimi on pakollinen")
            return

        if len(receipt_name) < 3:
            self._show_error("Maksun nimen pitää olla vähintää 3 merkkiä")
            return

        if receipt_name.isspace():
            self._show_error("Pelkkä välilyönti ei kelpaa")
            return

        if len(amount) == 0:
            self._show_error("Maksun summa on pakollinen")
            return

        try:
            float(amount)
        except ValueError:
            self._show_error("Maksun summa ei ole numero")
            return

        if payer == None or len(payer) == 0:
            self._show_error("Valitse maksaja")
            return

        if buyers == None or len(buyers) == 0:
            self._show_error("Valitse ostajat")
            return

        buyers_share = float(amount) / len(buyers)

        if payment_service.get_payment_by_travel_and_name(self._travel.travel_id, receipt_name):
            self._show_error(f"{receipt_name} on jo tallennettu")
            return

        try:
            payment_service.create_payment(
                self._travel.travel_id,
                receipt_name,
                date,
                amount,
                "maksu",
                payer[0],
                information
            )
            for buyer in buyers:
                payment_service.create_payment(
                    self._travel.travel_id,
                    receipt_name,
                    date,
                    str(buyers_share),
                    "ostos",
                    buyer,
                    information
                )
        except:
            self._show_error("Maksun tallentaminen epäonnistui")

        self._handle_create_payment()

    def _show_error(self, message):
        """Näyttää virheilmoituksen"""

        self._error_variable.set(message)
        self._error_label.grid(row=1, column=2)

    def _hide_error(self):
        """Poistaa virheilmoituksen näkyvistä"""

        self._error_label.grid_remove()

    def _initialize_receipt_name_field(self):
        """Alustaa kentä maksun nimi"""

        receipt_name_label = ttk.Label(master=self._frame, text="Maksun nimi")

        self._receipt_name_entry = ttk.Entry(master=self._frame)

        receipt_name_label.grid(row=1, column=0, padx=5,
                                pady=5, sticky=constants.W)
        self._receipt_name_entry.grid(
            row=1, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_amount_field(self):
        """Alustaa kentä maksun määrä"""

        amount_label = ttk.Label(master=self._frame, text="Maksun summa")

        self._amount_entry = ttk.Entry(master=self._frame)

        amount_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._amount_entry.grid(row=2, column=1, padx=5,
                                pady=5, sticky=constants.EW)

    def _initialize_date_field(self):
        """Alustaa kentä päivämäärä"""

        receipt_date_label = ttk.Label(master=self._frame, text="Päivämäärä")

        self._date_entry = DateEntry(master=self._frame, selectmode='day')

        receipt_date_label.grid(row=3, column=0, padx=5,
                                pady=5, sticky=constants.W)
        self._date_entry.grid(row=3, column=1, padx=5,
                              pady=5, sticky=constants.EW)

    def _initialize_payer_field(self):
        """Alustaa valintaruudun maksaja"""

        payer_label = ttk.Label(
            master=self._frame, text="Valitse maksaja")

        payers = []
        payer_list = participant_service.get_participants_by_guide_and_travel(
            self._guide, self._travel.travel_id)
        for payer in payer_list:
            payers.append(payer.name)

        payer_list = tk.Variable(value=list(payers))

        self._payer_selection = tk.Listbox(
            master=self._frame,
            listvariable=payer_list,
            height=len(payers),
            selectmode=tk.SINGLE,
            exportselection=False
        )

        payer_label.grid(row=4, column=0, padx=5,
                         pady=5, sticky=constants.W)
        self._payer_selection.grid(
            row=4, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_information_field(self):
        """Alustaa kentä maksun lisätiedot"""

        information_label = ttk.Label(
            master=self._frame, text="Maksun lisätiedot")

        self._information_entry = ttk.Entry(master=self._frame)

        information_label.grid(row=6, column=0, padx=5,
                               pady=5, sticky=constants.W)
        self._information_entry.grid(
            row=6, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_buyers_field(self):
        """Alustaa valintaruudun ostajat"""

        buyers_label = ttk.Label(
            master=self._frame, text="Valitse ostajat")

        buyers = []
        buyers_list = participant_service.get_participants_by_guide_and_travel(
            self._guide, self._travel.travel_id)
        for buyer in buyers_list:
            buyers.append(buyer.name)

        buyers_list = tk.Variable(value=list(buyers))

        self._buyers_selection = tk.Listbox(
            master=self._frame,
            listvariable=buyers_list,
            height=len(buyers),
            selectmode=tk.MULTIPLE,
            exportselection=False
        )

        buyers_label.grid(row=5, column=0, padx=5,
                          pady=5, sticky=constants.W)
        self._buyers_selection.grid(
            row=5, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_header(self):
        """Alustaa näkymän otsikon"""

        headline_label = ttk.Label(
            master=self._frame,
            text="Uusi maksu matkalle: " + self._travel.name
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

        self._initialize_header()
        self._initialize_receipt_name_field()
        self._initialize_amount_field()
        self._initialize_date_field()
        self._initialize_payer_field()
        self._initialize_buyers_field()
        self._initialize_information_field()

        create_travel_button = ttk.Button(
            master=self._frame,
            text="Lisää maksu",
            command=self._create_payment_handler
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._handle_cancel
        )

        self._frame.grid_columnconfigure(0, weight=1)

        create_travel_button.grid(row=7, column=1, padx=5,
                                  pady=5, sticky=constants.EW)
        cancel_button.grid(row=8, column=1, padx=5,
                           pady=7, sticky=constants.EW)

        self._hide_error()
