''' Implementación de lista ligada '''
from node import Node

class LinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head

        if (not self.counter):
            self.tail = self.head

        self.counter += 1

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        if not self.tail:
            self.headInsert(val)
            self.tail = self.head
            return

        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail
        self.counter += 1
    
    def headRemove(self) -> None:
        if not self.head:
            raise ValueError('La lista está vacía')

        self.head = self.head.next
        self.counter -= 1

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        curr = self.head

        if not curr:
            print('La lista está vacía')
            return

        cnt = 1

        while curr:
            print(f'Nodo #{cnt} -> {curr.val}')
            curr = curr.next
            cnt += 1

if __name__ == '__main__':
    lista_ligada = LinkedList()
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llenado de la lista
    for i in lista_tradicional:
        lista_ligada.tailInsert(i)

    # Impresión de la lista
    print('Impresión #1 -> Llenado de lista')
    lista_ligada.traverse()

    # Adición de un nuevo elemento al final
    print('\nImpresión #2 -> Nuevo elemento al final')
    n = False
    lista_ligada.tailInsert(n)
    lista_ligada.traverse()

    # Adición de un nuevo elemento al inicio
    print('\nImpresión #3 -> Nuevo elemento al inicio')
    n = 'Estructuras'
    lista_ligada.headInsert(n)
    lista_ligada.traverse()

    # Eliminación del primer elemento e impresión
    print('\nImpresión #4 -> Eliminación del primer elemento')
    lista_ligada.headRemove()
    lista_ligada.traverse()

    # Eliminación del último elemento (o explica por qué no es posible en un comentario multilínea)