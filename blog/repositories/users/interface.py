from abc import ABC, abstractmethod

from blog.user import User
from blog.uuid import UUID


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def get(self, uuid: UUID) -> User: ...

    @abstractmethod
    def get_by_username(self, username: str) -> User: ...

    @abstractmethod
    def delete(self, uuid: UUID) -> None: ...

    @abstractmethod
    def get_all(self) -> list[User]: ...
