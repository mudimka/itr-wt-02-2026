"""Интернет-магазин (урок 1): все классы в одном файле."""
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


class FeedbackForm:
    """Форма обратной связи: сообщение от пользователя с email для ответа."""

    def __init__(self, email, message):
        self.email = email  # проходит через сеттер с проверкой
        self.message = message
        self.sent = False

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email must contain '@'")
        self._email = value

    def send(self):
        """Отправить форму (имитация); пустое сообщение отправить нельзя."""
        if not self.message.strip():
            raise ValueError("Message must not be empty")
        self.sent = True
        return f"Сообщение от {self.email} отправлено"


if __name__ == "__main__":
    # абстрактный товар создать нельзя
    try:
        Product("x", 1)
    except TypeError as error:
        print(f"Нельзя создать абстрактный Product: {error}")

    anna = User("Анна", "anna@example.com")
    boss = Admin("Борис", "boss@example.com")

    book = DigitalProduct("Python для начинающих", 500)
    mouse = PhysicalProduct("Мышь", 1500)
    sofa = HeavyProduct("Диван", 30000, weight=40)

    # полиморфизм: один цикл, один метод, разные классы
    for product in (book, mouse, sofa):
        print(f"{product.name}: доставка {product.delivery_cost()} руб.")

    cart = Cart(anna)
    for product in (book, mouse, sofa):
        cart.add(product)
    print(len(cart))
    print(cart)

    # отзывы
    review = anna.write_review(mouse, 5, "Отличная мышь")
    bad = anna.write_review(mouse, 2, "Скрипит")
    print(review, "| положительный:", review.is_positive())
    print("Средняя оценка:", mouse.average_rating())
    boss.delete_review(mouse, bad)
    print("После удаления:", mouse.average_rating())

    # проверки
    for action in (lambda: DigitalProduct("Бесплатно", 0), lambda: anna.write_review(mouse, 6)):
        try:
            action()
        except ValueError as error:
            print("Ошибка:", error)

    form = FeedbackForm("anna@example.com", "Спасибо за магазин!")
    print(form.send())
