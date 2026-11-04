"""Пользователи интернет-магазина."""


class User:
    """Покупатель магазина с именем и email."""

    def __init__(self, name, email):
        self.name = name
        self.email = email  # проходит через сеттер с проверкой

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email must contain '@'")
        self._email = value

    def write_review(self, product, rating, text=""):
        """Написать отзыв на товар и прикрепить его к товару."""
        from shop.review import Review  # импорт внутри метода: нет цикла на уровне модулей

        review = Review(self, product, rating, text)
        product.add_review(review)
        return review

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Admin(User):
    """Администратор: отличается от пользователя тем, что может удалять отзывы."""

    def delete_review(self, product, review):
        """Удалить отзыв у товара."""
        product.reviews.remove(review)
