"""Товары интернет-магазина."""
from abc import ABC, abstractmethod


class Product(ABC):
    """Абстрактный товар: у каждого вида товара своя стоимость доставки."""

    def __init__(self, name, price):
        self.name = name
        self.price = price  # проходит через сеттер с проверкой
        self.reviews = []  # свой список отзывов у каждого товара

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        self._price = value

    @abstractmethod
    def delivery_cost(self):
        """Стоимость доставки; каждый наследник считает по-своему."""

    def add_review(self, review):
        """Добавить отзыв к товару."""
        self.reviews.append(review)

    def average_rating(self):
        """Средняя оценка по отзывам (0, если отзывов нет)."""
        if not self.reviews:
            return 0
        return sum(r.rating for r in self.reviews) / len(self.reviews)

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"


class PhysicalProduct(Product):
    """Обычный физический товар: отличается от базового фиксированной доставкой 300 руб."""

    DELIVERY_PRICE = 300

    def delivery_cost(self):
        return self.DELIVERY_PRICE


class DigitalProduct(Product):
    """Цифровой товар: отличается тем, что доставка не нужна (стоит 0)."""

    def delivery_cost(self):
        return 0


class HeavyProduct(PhysicalProduct):
    """Тяжёлый товар: отличается наличием веса, доставка считается по весу."""

    PRICE_PER_KG = 50

    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def delivery_cost(self):
        return self.DELIVERY_PRICE + self.weight * self.PRICE_PER_KG
