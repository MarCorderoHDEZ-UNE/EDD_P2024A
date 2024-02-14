''' Implementación de lista circular '''
from node import Node

class CircularLinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
    
    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''

if __name__ == '__main__':
    lista_circular = CircularLinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llenado de la lista
    ...

    # Impresión de la lista
    ...

    # Adición de un nuevo elemento al final
    n = False
    ...

    # Adición de un nuevo elemento al inicio
    n = 'Estructuras'
    ...

    # Eliminación del primer elemento e impresión
    ...
