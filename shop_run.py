"""Точка запуска: примеры работы с пакетом shop."""
from shop.product import DigitalProduct as Ebook, HeavyProduct, PhysicalProduct, Product
from shop.cart import Cart
from shop.user import Admin, User
from shop.feedback import FeedbackForm

if __name__ == "__main__":
    # абстрактный товар создать нельзя
    try:
        Product("x", 1)
    except TypeError as error:
        print(f"Нельзя создать абстрактный Product: {error}")

    anna = User("Анна", "anna@example.com")
    boss = Admin("Борис", "boss@example.com")

    book = Ebook("Python для начинающих", 500)
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
    for action in (lambda: Ebook("Бесплатно", 0), lambda: anna.write_review(mouse, 6)):
        try:
            action()
        except ValueError as error:
            print("Ошибка:", error)

    form = FeedbackForm("anna@example.com", "Спасибо за магазин!")
    print(form.send())
