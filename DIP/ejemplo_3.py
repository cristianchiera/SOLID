class EmailSender:
    def send_email(self, message: str) -> None:
        print(f"Enviando email: {message}")

class SMSSender:
    def send_sms(self, message: str) -> None:
        print(f"Enviando SMS: {message}")

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()
        self.sms_sender = SMSSender()

    def send_notification(self, message: str, method: str) -> None:
        if method == "email":
            self.email_sender.send_email(message)
        elif method == "sms":
            self.sms_sender.send_sms(message)
        else:
            raise ValueError("Método de notificación no soportado")

# Uso
service = NotificationService()
service.send_notification("Hola mundo", "email")
service.send_notification("Hola mundo", "sms")