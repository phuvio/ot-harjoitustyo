from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database
from database_connection import get_database_connection
from services.travel_service import TravelService
from services.user_services import UserService
from repositories.travel_repository import TravelRepository
from repositories.user_repository import UserRepository


def main():
    travel_service = TravelService(TravelRepository(get_database_connection()))
    user_service = UserService(UserRepository(get_database_connection))
    initialize_database()
    window = Tk()
    window.geometry("500x400")
    window.title("Matkakululaskuri")

    ui_view = UI(window, travel_service, user_service)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
