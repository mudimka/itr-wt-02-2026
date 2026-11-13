import sqlite3

from blog.exceptions import UserNotFoundException
from blog.person.name import Name
from blog.repositories.users.in_memory import InMemoryUsersRepository
from blog.repositories.users.interface import UserRepository
from blog.repositories.users.sqlite import SqliteUsersRepository
from blog.user import User
from blog.uuid import UUID
from init_db import create_schema


def check_delete(title: str, repository: UserRepository) -> None:
    print(f"--- {title} ---")
    user = User(UUID.random(), "ivan", Name("Иван", "Иванов"))
    repository.save(user)
    print("до удаления:", repository.get(user.uuid))

    repository.delete(user.uuid)

    try:
        repository.get(user.uuid)
    except UserNotFoundException as error:
        print("после удаления get бросает:", error)
    else:
        raise AssertionError("get() must raise after delete()")

    try:
        repository.delete(UUID.random())
    except UserNotFoundException as error:
        print("delete несуществующего бросает:", error)
    else:
        raise AssertionError("delete() of unknown uuid must raise")


def make_sqlite_repository() -> UserRepository:
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    return SqliteUsersRepository(connection)


if __name__ == "__main__":
    check_delete("InMemory", InMemoryUsersRepository())
    check_delete("Sqlite", make_sqlite_repository())
    print("OK")
