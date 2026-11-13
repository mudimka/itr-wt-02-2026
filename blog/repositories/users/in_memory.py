from blog.exceptions import UserNotFoundException
from blog.repositories.users.interface import UserRepository
from blog.user import User
from blog.uuid import UUID


class InMemoryUsersRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def save(self, user: User) -> None:
        self._users[user.uuid] = user

    def get(self, uuid: UUID) -> User:
        if uuid not in self._users:
            raise UserNotFoundException(f"User not found: {uuid}")
        return self._users[uuid]

    def get_by_username(self, username: str) -> User:
        for user in self._users.values():
            if user.username == username:
                return user
        raise UserNotFoundException(f"User not found: {username}")

    def delete(self, uuid: UUID) -> None:
        if uuid not in self._users:
            raise UserNotFoundException(f"User not found: {uuid}")
        del self._users[uuid]

    def get_all(self) -> list[User]:
        # новый список: изменение результата не затрагивает репозиторий
        return list(self._users.values())
