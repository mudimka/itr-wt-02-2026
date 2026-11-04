"""Корзина покупателя."""
from shop.product import Product


class Cart:
    """Корзина: хранит товары одного пользователя и считает итоговую сумму."""

    def __init__(self, owner):
        self.owner = owner
        self.items = []  # свой список у каждой корзины

    def add(self, product):
        """Положить товар в корзину."""
        if not isinstance(product, Product):
            raise TypeError("Only Product can be added to cart")
        self.items.append(product)

    def total(self):
        """Сумма товаров без доставки."""
        return sum(p.price for p in self.items)

    def delivery_total(self):
        """Суммарная доставка: полиморфный вызов delivery_cost() у разных товаров."""
        return sum(p.delivery_cost() for p in self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        lines = [f"Корзина {self.owner.name}:"]
        lines += [f"  - {p}" for p in self.items]
        lines.append(f"Итого: {self.total()} руб. + доставка {self.delivery_total()} руб.")
        return "\n".join(lines)
