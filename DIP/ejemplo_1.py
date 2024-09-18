
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Conectando a MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Conectando a PostgreSQL"

class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        return self.database.connect()

# Uso de las clases
mysql_db = MySQLDatabase()
app = Application(mysql_db)
print(app.start())

postgres_db = PostgreSQLDatabase()
app = Application(postgres_db)
print(app.start())
