''' Implementador '''
from Nodo import Nodo

def recorrido(head:Nodo) -> None:
    cnt = 1

    while (head):
        print(f'Nodo #{cnt} -> {head}')
        head = head.next
        cnt += 1
    
    print()

def rellenado_while(elementos:list) -> Nodo:
    ''' Función para implementar lista ligada con while '''
    head = Nodo()
    curr = head

    while elementos:
        curr.val = elementos.pop(0)
        curr.next = Nodo()
        curr = curr.next

    return head

def rellenado_for(elementos:list) -> Nodo:
    head = Nodo()
    curr = head

    for e in elementos:
        curr.val = e
        curr.next = Nodo()
        curr = curr.next
    
    return head

if __name__ == '__main__':
    lista = list(range(1, 6))
    print(f'Lista original: {lista}')
    head = rellenado_while(lista)
    recorrido(head)

    lista = list(range(1, 21, 2))
    head = rellenado_for(lista)
    print(f'Lista original: {lista}')
    recorrido(head)
