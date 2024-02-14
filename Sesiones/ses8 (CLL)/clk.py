''' Implementación de listas ligadas circulares '''
from Nodo import Nodo

def show(head:Nodo) -> None:
    curr = head
    cnt = 1

    while True:
        print(f'Nodo #{cnt}: {curr.val}')
        curr = curr.next
        cnt += 1

        if curr == head:
            print('⤷ Retorna al inicio de la lista')
            return

def fill(elems:list) -> Nodo:
    # 1 2 3 4 5 6 7; len = 7
    # 0 1 2 3 4 5 6; len - 1 = 6
    head = Nodo()
    curr = head

    for i in range(len(elems)-1):
        curr.val = elems[i]
        curr.next = Nodo()
        curr = curr.next
    
    curr.val = elems[-1]
    curr.next = head
    return head

if __name__ == '__main__':
    elems = range(1, 11)
    head = fill(elems)
    show(head)