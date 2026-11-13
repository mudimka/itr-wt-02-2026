import sqlite3
from pathlib import Path

from blog.exceptions import UserNotFoundException
from blog.person.name import Name
from blog.repositories.users.sqlite import SqliteUsersRepository
from blog.user import User
from blog.uuid import UUID

connection = sqlite3.connect(Path(__file__).parent / "blog.sqlite")
users_repository = SqliteUsersRepository(connection)

uuid = UUID.random()
users_repository.save(User(uuid, f"ivan_{str(uuid)[:8]}", Name("Иван", "Иванов")))

try:
    print(users_repository.get(uuid))
    print(users_repository.get(UUID.random()))
except UserNotFoundException as error:
    print(error)
