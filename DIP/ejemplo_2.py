class Database:
    def connect(self):
        print("Conectando a la base de datos...")

class Application:
    def __init__(self):
        self.db = Database()

    def run(self):
        self.db.connect()
        print("Aplicación ejecutándose...")



app = Application()
app.run()