from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def mover(self):
        pass

class AveVoladora(Ave):
    def mover(self):
        print("Esta ave está volando")

class AveNoVoladora(Ave):
    def mover(self):
        print("Esta ave está caminando")

class Golondrina(AveVoladora):
    pass

class Pinguino(AveNoVoladora):
    pass

def hacer_mover_ave(ave: Ave):
    ave.mover()

# Uso
golondrina = Golondrina()
pinguino = Pinguino()

hacer_mover_ave(golondrina)  # Imprime: Esta ave está volando
hacer_mover_ave(pinguino)    # Imprime: Esta ave está caminando