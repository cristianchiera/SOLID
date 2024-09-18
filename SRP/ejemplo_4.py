
from abc import ABC, abstractmethod

class Luz(ABC):
    @abstractmethod
    def encender(self):
        pass
    
    @abstractmethod
    def apagar(self):
        pass

class LuzBlanca(Luz):
    def encender(self):
        print("Luz encendida blanca")
    
    def apagar(self):
        print("Luz apagada blanca")

class LuzAmarilla(Luz):
    def encender(self):
        print("Luz encendida Amarilla")
    
    def apagar(self):
        print("Luz apagada Amarilla")

class ControladorLuz:
    def __init__(self, luz: Luz):
        self.luz = luz
    
    def encender_luz(self):
        self.luz.encender()
    
    def apagar_luz(self):
        self.luz.apagar()

# Uso
luz_blanca = LuzBlanca()
controlador_blanca = ControladorLuz(luz_blanca)
controlador_blanca.encender_luz()
controlador_blanca.apagar_luz()

luz_amarilla = LuzAmarilla()
controlador_amarilla = ControladorLuz(luz_amarilla)
controlador_amarilla.encender_luz()
controlador_amarilla.apagar_luz()