''' Módulo contenedor de clase Nodo para listas ligadas '''

class Nodo:
    ''' Clase de Nodo '''

    def __init__(self, val:int = None):
        ''' Inicializador de clase '''
        self.val = val
        self.next = None
    
    def __str__(self) -> str:
        if self.val:
            return f'Valor del nodo = {self.val}'
        
        return f'El nodo no tiene valor'
