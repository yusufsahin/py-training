import sqlite3
from pathlib import Path


def create_connection():
    current_dir = Path(__file__).parent
    db_path = current_dir / "myDb.sqlite"

    return sqlite3.connect(db_path)


def create_table(conn):
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            salary NUMERIC
        )
        """)


def insert_employee(conn, name, salary):
    with conn:
        conn.execute("""
        INSERT INTO employees (name, salary)
        VALUES (?, ?)
        """, (name, salary))


def fetch_employees(conn):
    cursor = conn.execute("SELECT id, name, salary FROM employees")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def main():
    conn = create_connection()

    try:
        print("SQLite database connected.")

        create_table(conn)

        insert_employee(conn, "John Doe", 50000)
        insert_employee(conn, "Jane Doe", 60000)

        fetch_employees(conn)

    finally:
        conn.close()


if __name__ == "__main__":
    main()