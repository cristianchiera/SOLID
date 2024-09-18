class Ave:
    def volar(self):
        print("Esta ave está volando")

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no pueden volar")

def hacer_volar_ave(ave: Ave):
    ave.volar()

# Uso
golondrina = Ave()
pinguino = Pinguino()

hacer_volar_ave(golondrina)
try:
    hacer_volar_ave(pinguino) 
 # Funciona bien
except Exception as e:
    print(f"Error->{e}")   # Lanza una excepción