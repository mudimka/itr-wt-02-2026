import sqlite3

from blog.person.name import Name
from blog.repositories.users.in_memory import InMemoryUsersRepository
from blog.repositories.users.interface import UserRepository
from blog.repositories.users.sqlite import SqliteUsersRepository
from blog.user import User
from blog.uuid import UUID
from init_db import create_schema


def check_get_all(title: str, repository: UserRepository) -> None:
    print(f"--- {title} ---")
    assert repository.get_all() == []
    print("пустой репозиторий:", repository.get_all())

    first = User(UUID.random(), "ivan", Name("Иван", "Иванов"))
    second = User(UUID.random(), "petr", Name("Пётр", "Петров"))
    repository.save(first)
    repository.save(second)

    users = repository.get_all()
    assert len(users) == 2
    assert {user.username for user in users} == {"ivan", "petr"}
    for user in users:
        print(user)

    users.clear()  # изменение результата не должно влиять на репозиторий
    assert len(repository.get_all()) == 2
    print("после очистки копии в репозитории:", len(repository.get_all()))


def make_sqlite_repository() -> UserRepository:
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    return SqliteUsersRepository(connection)


if __name__ == "__main__":
    check_get_all("InMemory", InMemoryUsersRepository())
    check_get_all("Sqlite", make_sqlite_repository())
    print("OK")
