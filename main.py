from datetime import datetime

from blog.person.name import Name
from blog.person.person import Person
from blog.post import Post
from blog.uuid import UUID

print(
    Post(
        author=Person(
            name=Name(first_name="Иван", last_name="Иванов"), registered_on=datetime.now()
        ),
        text="некоторый текст",
    )
)

print(UUID(None))
