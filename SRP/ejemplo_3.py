class Luz:
    def encender(self):
        print("Luz encendida")
    
    def apagar(self):
        print("Luz apagada")

class ControladorLuz:
    def __init__(self):
        self.luz = Luz()
    
    def encender_luz(self):
        self.luz.encender()
    
    def apagar_luz(self):
        self.luz.apagar()

# Uso
controlador = ControladorLuz()
controlador.encender_luz()
controlador.apagar_luz()