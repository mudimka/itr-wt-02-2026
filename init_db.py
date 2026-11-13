import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    uuid TEXT NOT NULL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
"""


def create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(SCHEMA)


if __name__ == "__main__":
    db_path = Path(__file__).parent / "blog.sqlite"
    connection = sqlite3.connect(db_path)
    create_schema(connection)
    connection.close()
    print(f"База данных готова: {db_path.name}")
