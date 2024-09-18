from abc import ABC, abstractmethod
from typing import Protocol

class MessageSender(Protocol):
    def send_message(self, message: str) -> None:
        ...

class EmailSender:
    def send_message(self, message: str) -> None:
        print(f"Enviando email: {message}")

class SMSSender:
    def send_message(self, message: str) -> None:
        print(f"Enviando SMS: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send_notification(self, message: str) -> None:
        self.sender.send_message(message)

# Uso
email_service = NotificationService(EmailSender())
email_service.send_notification("Hola mundo")

sms_service = NotificationService(SMSSender())
sms_service.send_notification("Hola mundo")