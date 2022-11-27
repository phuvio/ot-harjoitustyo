from ui.travels_view import TravelView
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka"""

    def __init__(self, root, travel_service, user_service):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan

        Args:
            root: Tkinter-elemnetti, jonka sisään käyttöliittymä alustetaan
            travel_service: travel_service-luokan importaaminen
            user_service: user_service-luokan importaaminen
        """

        self._root = root
        self._current_view = None
        self._travel_service = travel_service
        self._user_service = user_service

    def start(self):
        """Käynnistää käyttöliittymän"""

        self._show_login_view()

    def _hide_current_view(self):
        """Poistaa nykyisen näkymän"""

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_travel_view(self):
        """Näyttää Matkat-näkymän"""

        self._hide_current_view()

        self._current_view = TravelView(self._root, self._travel_service)

        self._current_view.pack()

    def _show_login_view(self):
        """Näyttää sisäänkirjautumisnäkymän"""

        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_travel_view,
            self._show_create_user_view,
            self._user_service
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        """Näyttää Luo uusi käyttäjä -näkymän"""

        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_travel_view,
            self._show_login_view,
            self._user_service
        )

        self._current_view.pack()
