"""Дополнительные упражнения к уроку 1."""


# Упражнение 1. BankAccount
class BankAccount:
    """Банковский счёт владельца с неотрицательным балансом."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # через сеттер: отрицательное значение даст ValueError

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        """Положить деньги на счёт."""
        self.balance = self._balance + amount

    def withdraw(self, amount):
        """Снять деньги; при нехватке средств сеттер бросит ValueError."""
        self.balance = self._balance - amount


# Упражнение 2. Shape -> Circle / Rectangle
class Shape:
    """Базовая фигура."""

    PI = 3.14

    def area(self):
        raise NotImplementedError("Subclass must implement area()")


class Circle(Shape):
    """Круг с радиусом."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2


class Rectangle(Shape):
    """Прямоугольник со сторонами."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Упражнение 3. Library и Book (композиция)
class Book:
    """Книга с названием и автором."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    """Библиотека, хранящая коллекцию книг."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book can be added to library")
        self._books.append(book)

    def find_by_author(self, author):
        return [b for b in self._books if b.author == author]

    def count(self):
        return len(self._books)


if __name__ == "__main__":
    acc = BankAccount("Анна", 100)
    print(acc.balance)
    for action in (lambda: setattr(acc, "balance", -5), lambda: acc.withdraw(500),
                   lambda: BankAccount("Анна", -1)):
        try:
            action()
        except ValueError as error:
            print("Ошибка:", error, "| баланс:", acc.balance)
    acc.deposit(50)
    print(acc.balance)

    for s in (Circle(1), Rectangle(2, 5)):
        print(s.area())
    try:
        Shape().area()
    except NotImplementedError as error:
        print("Ошибка:", error)

    l1, l2 = Library(), Library()
    l1.add_book(Book("Мастер и Маргарита", "Булгаков"))
    print(l1.count(), l2.count(), len(l1.find_by_author("Пушкин")))
    try:
        l1.add_book("не книга")
    except TypeError as error:
        print("Ошибка:", error)
