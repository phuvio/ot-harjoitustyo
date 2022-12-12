from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantaulut

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists travels
    """)

    cursor.execute("""
        drop table if exists users
    """)

    cursor.execute("""
        drop table if exists participants
    """)

    cursor.execute("""
        drop table if exists payments
    """)

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS travels (
            name TEXT,
            guide TEXT,
            travel_id INTEGER PRIMARY KEY
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS participants (
            name TEXT,
            travel TEXT,
            guide TEXT,
            participant_id INTEGER PRIMARY KEY
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            travel INTEGER,
            receipt_name TEXT,
            date TEXT,
            amount TEXT,
            action TEXT,
            payer TEXT,
            information TEXT,
            payment_id INTEGER PRIMARY KEY
        )
    """)

    print("Database created successfully")

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut"""

    connection = get_database_connection()

    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
