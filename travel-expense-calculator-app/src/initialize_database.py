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
            name TEXT PRIMARY KEY,
            participants TEXT
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
            name TEXT PRIMARY KEY,
            travel TEXT,
            guide TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            name TEXT PRIMARY KEY,
            date TEXT,
            sum NUMERIC,
            action TEXT,
            payer TEXT,
            info TEXT
        )
    """)

    print("Database created successfully")

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut"""

    connection = get_database_connection()

    # drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
