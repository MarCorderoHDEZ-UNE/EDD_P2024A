''' Nodo con doble referencia '''

class NodoDoble:
    def __init__(self, val:int|str = None):
        self.val = val
        self.prev:NodoDoble = None
        self.next:NodoDoble = None
    
    def __str__(self) -> str:
        return str(self.val) if self.val else '∅'