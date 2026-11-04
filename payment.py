"""Задача 1: абстрактный класс PaymentMethod."""
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Абстрактный способ оплаты."""

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def pay(self, amount):
        """Оплатить сумму; реализуется в наследниках."""

    def describe(self):
        """Напечатать название способа оплаты."""
        print(f"Способ оплаты: {self.title}")


class CardPayment(PaymentMethod):
    """Оплата банковской картой."""

    def __init__(self, card_number):
        super().__init__("Карта")
        self.card_number = card_number

    def pay(self, amount):
        return f"Оплачено {amount} картой ****{self.card_number[-4:]}"


class CashPayment(PaymentMethod):
    """Оплата наличными."""

    def __init__(self):
        super().__init__("Наличные")

    def pay(self, amount):
        return f"Принято {amount} наличными"


if __name__ == "__main__":
    try:
        PaymentMethod("x")
    except TypeError as error:
        print(f"Нельзя создать абстрактный класс: {error}")

    class Broken(PaymentMethod):
        """Наследник без pay."""

    try:
        Broken("broken")
    except TypeError as error:
        print(f"Наследник без pay не создаётся: {error}")

    for method in (CardPayment("1234567812345678"), CashPayment()):
        method.describe()
        print(method.pay(100))
