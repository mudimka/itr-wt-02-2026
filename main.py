from datetime import datetime

from blog.comment import Comment
from blog.person.name import Name
from blog.person.person import Person
from blog.post import Post

post_author = Person(name=Name(first_name="Иван", last_name="Иванов"), registered_on=datetime.now())
post = Post(author=post_author, text="некоторый текст")

comment_author = Person(
    name=Name(first_name="Пётр", last_name="Петров"), registered_on=datetime.now()
)
comment = Comment(author=comment_author, post=post, text="отличный пост")

print(post)
print(comment)
