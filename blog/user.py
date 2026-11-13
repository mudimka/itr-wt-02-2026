from dataclasses import dataclass

from blog.person.name import Name
from blog.uuid import UUID


@dataclass
class User:
    uuid: UUID
    username: str
    name: Name

    def __str__(self) -> str:
        return f"Пользователь {self.username}: {self.name}"
