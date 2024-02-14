''' Implementación de lista doblemente ligada '''

from Nodo import NodoDoble

def full_show(head:NodoDoble, object_mode:bool = False) -> None:
    curr = head
    cnt = 1

    while curr.val:
        print(f'Nodo #{cnt}: {curr.val}, ', end="")
        print(f'Previo: {curr.prev if object_mode else curr.prev.val if curr.prev else "∅"}, ', end="")
        print(f'Siguiente: {curr.next if object_mode else curr.next.val if curr.next else "∅"}')

        curr = curr.next
        cnt += 1

def show(head:NodoDoble) -> None:
    curr = head

    while curr is not None:
        if (not curr.prev):
            print('<->', end='')

        print(curr, end='')

        if (not curr.next):
            print()
            return
        else:
            print('<->', end='')
            curr = curr.next

def fill(elems:list) -> NodoDoble:
    head = NodoDoble()
    curr = prev = head

    while elems:
        curr.val = elems.pop(0)
        curr.next = NodoDoble()
        prev = curr
        curr = curr.next
        curr.prev = prev
    
    return head

if __name__ == '__main__':
    elems = list('CORDERO')
    head = fill(elems)

    show(head)

    new_head = head.next.next.next
    # print(new_head)
    print()

    full_show(head)
    print()
    full_show(head, True)

