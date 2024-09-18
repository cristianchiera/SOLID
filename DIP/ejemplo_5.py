from abc import ABC, abstractmethod

# Abstracción
class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

# Implementación concreta de la abstracción
class MySQLDatabase(DatabaseInterface):
    def connect(self) -> None:
        print("Conectando a la base de datos MySQL...")

# Otra implementación concreta (puede ser un mock para pruebas)
class TestDatabase(DatabaseInterface):
    def connect(self) -> None:
        print("Simulando conexión a la base de datos para pruebas...")

# Aplicación que depende de la abstracción
class Application:
    def __init__(self, db: DatabaseInterface) -> None:
        self.db = db

    def run(self) -> None:
        self.db.connect()
        print("Aplicación ejecutándose...")

# Uso del código refactorizado
if __name__ == "__main__":
    db = MySQLDatabase()  # O TestDatabase() para pruebas
    app = Application(db)
    app.run()

    # Pruebas
    print("\nPruebas:\n")
    db2=TestDatabase()
    app2=Application(db2)
    app2.run()
