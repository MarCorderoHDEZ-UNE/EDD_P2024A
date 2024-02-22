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
        new_head = Node(val)

        if not self.head:
            self.head = new_head
            self.tail = self.head
        else:
            new_head.next = self.head
            self.head = new_head
        
        self.tail.next = self.head
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
        self.tail.next = self.head
        self.counter += 1
    
    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''

        if not self.head:
            raise ValueError('La lista está vacía')

        if self.counter == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

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

            if curr == self.head:
                print('⤷ Retorna al inicio de la lista')
                break

if __name__ == '__main__':
    lista_circular = CircularLinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

   # Llenado de la lista
    for i in lista_tradicional:
        lista_circular.tailInsert(i)

    # Impresión de la lista
    print('Impresión #1 -> Llenado de lista')
    lista_circular.traverse()

    # Adición de un nuevo elemento al final
    print('\nImpresión #2 -> Nuevo elemento al final')
    n = False
    lista_circular.tailInsert(n)
    lista_circular.traverse()

    # Adición de un nuevo elemento al inicio
    print('\nImpresión #3 -> Nuevo elemento al inicio')
    n = 'Estructuras'
    lista_circular.headInsert(n)
    lista_circular.traverse()

    # Eliminación del primer elemento e impresión
    print('\nImpresión #4 -> Eliminación del primer elemento')
    lista_circular.headRemove()
    lista_circular.traverse()
