"""Форма обратной связи."""


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
