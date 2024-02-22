''' Implementación de lista dinámica '''
import ctypes

class ListaDinamica:
    def __init__(self) -> None:
        ''' Inicializar un arreglo vacío '''
        self.__n = 0                                 # Elementos actuales
        self._capacidad = 1                         # Capacidad inicial por defecto
        self.__A = self._init_arr(self._capacidad)   # Arreglo contenedor

    def __len__(self) -> int:
        ''' Regresa la cantidad de elementos almacenados en la lista '''
        return self.__n

    def __getitem__(self, k) -> object:
        ''' Regresa un elemento en una posición k '''
        if k < 0:
            if abs(k) > self.__n:
                raise IndexError(f'Índice inválido ({k})')
            k = self.__n + k
        elif k >= self.__n:
            raise IndexError(f'Índice inválido ({k})')
        
        return self.__A[k]
    
    def append(self, obj) -> None:
        ''' Añade un elemento al final de la lista '''
        if self.__n == self._capacidad:
            self._resize(2 * self._capacidad)
        
        self.__A[self.__n] = obj
        self.__n += 1

    def _resize(self, c) -> None:
        ''' Modifica el tamaño de la lista interna '''
        B = self._init_arr(c)

        for k in range(self.__n):
            B[k] = self.__A[k]

        self.__A = B
        self._capacidad = c

    def _init_arr(self, capacidad):
        ''' Regresa un nuevo arreglo con capacidad determinada '''
        return (capacidad * ctypes.py_object)()     # Magia

if ___name__ == '__main__':
    ''' Pruebas de la clase '''
    # 1. Instanciación
    ld = ListaDinamica()

    # 2. Inserción de al menos 5 elementos
    ld.append(10)
    ld.append(20)
    ld.append(False)
    ld.append(-0.53)
    ld.append('String')

    # 3. Impresión de los elementos usando for
    for i in range(1, len(ld)+1):
        print(ld[-i])
