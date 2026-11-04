from dataclasses import dataclass

from blog.person.person import Person
from blog.post import Post


@dataclass
class Comment:
    """Комментарий пользователя к посту."""

    author: Person
    post: Post
    text: str

    def __str__(self) -> str:
        return f"{self.author.name}: {self.text}"
