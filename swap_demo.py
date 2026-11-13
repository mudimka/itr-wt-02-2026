import sqlite3

from blog.person.name import Name
from blog.repositories.users.in_memory import InMemoryUsersRepository
from blog.repositories.users.interface import UserRepository
from blog.repositories.users.sqlite import SqliteUsersRepository
from blog.user import User
from blog.uuid import UUID
from init_db import create_schema


def make_sqlite_repository() -> UserRepository:
    # sqlite3 нужен только здесь: код ниже о нём ничего не знает
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    return SqliteUsersRepository(connection)


# Реализация меняется ОДНОЙ строкой: оставьте нужную, вторую закомментируйте.
users_repository: UserRepository = InMemoryUsersRepository()
# users_repository: UserRepository = make_sqlite_repository()

# Интерфейс UserRepository гарантирует, что у любой реализации есть методы save/get/
# get_by_username с одинаковыми аргументами и результатом, поэтому код ниже не зависит от
# того, где именно хранятся пользователи.
users_repository.save(User(UUID.random(), "ivan", Name("Иван", "Иванов")))
users_repository.save(User(UUID.random(), "petr", Name("Пётр", "Петров")))

print(users_repository.get_by_username("ivan"))
print(users_repository.get_by_username("petr"))
