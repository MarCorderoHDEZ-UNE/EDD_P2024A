''' Implementación de lista doblemente ligada '''
from node import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def isEmpty(self) -> bool:
        ''' Mostrar si la lista está vacía '''

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
    
    def insertBetween(self, prev, val) -> None:
        ''' Insertar elemento entre dos nodos '''

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
    
    def headDelete(self) -> None:
        ''' Eliminar el primer elemento de la lista '''
    
    def tailDelete(self) -> None:
        ''' Eliminar el último elemento de la lista '''

    def deleteBetween(self, val) -> None:
        ''' Eliminar elemento entre dos nodos '''

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''

if __name__ == '__main__':
    lista_doblemente_ligada = DoubleLinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

   # Llenado de la lista
    ...

    # Impresión de la lista
    print('Impresión #1 -> Llenado de lista')
    ...

    # Adición de un nuevo elemento al final
    print('\nImpresión #2 -> Nuevo elemento al final')
    n = False
    ...

    # Adición de un nuevo elemento al inicio
    print('\nImpresión #3 -> Nuevo elemento al inicio')
    n = 'Estructuras'
    ...

    # Adición de elemento entre dos nodos
    print('\nImpresión #4 -> Nuevo elemento entre dos nodos')
    prev, n = True, False
    ...

    # Eliminación del primer elemento e impresión
    print('\nImpresión #5 -> Eliminación del primer elemento')
    ...
    
    # Eliminación del último elemento e impresión
    print('\nImpresión #6 -> Eliminación del último elemento')
    ...
    
    # Eliminación del primer elemento e impresión
    print('\nImpresión #7 -> Eliminación de elemento en la lista')
    n = 3
    ...
