"""Задача 2: класс Money."""


class Money:
    """Денежная сумма с валютой."""

    def __init__(self, amount, currency="RUB"):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"Money(amount={self.amount!r}, currency={self.currency!r})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __hash__(self):
        return hash((self.amount, self.currency))

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies")
        return Money(self.amount + other.amount, self.currency)


if __name__ == "__main__":
    a, b = Money(5), Money(7)
    print(a, repr(a))
    print(a == Money(5), a == b, Money(5, "USD") == a, a == 5)
    print(a + b, a, b)
    try:
        Money(5, "USD") + a
    except ValueError as error:
        print("Ошибка:", error)
