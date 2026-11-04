"""Отзывы на товары."""


class Review:
    """Отзыв пользователя на товар с оценкой от 1 до 5."""

    def __init__(self, user, product, rating, text=""):
        self.user = user  # композиция: отзыв хранит пользователя и товар
        self.product = product
        self.rating = rating  # проходит через сеттер с проверкой
        self.text = text

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

    def is_positive(self):
        """Отзыв положительный, если оценка 4 или выше."""
        return self.rating >= 4

    def __str__(self):
        return f"{self.user.name} про «{self.product.name}»: {self.rating}/5"
