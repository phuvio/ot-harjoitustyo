from tkinter import Tk, ttk
from ui.travels_view import TravelView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_travel_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_travel_view(self):
        self._hide_current_view()

        self._current_view = TravelView(self._root)

        self._current_view.pack()
