from objetos import Animal

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def maullar(self):
        print('Miau')

if __name__ == '__main__':
    perro = Animal('Firulaius')
    # perro.maullar()

    gato = Gato('Michi')
    print(gato)
    gato.maullar()