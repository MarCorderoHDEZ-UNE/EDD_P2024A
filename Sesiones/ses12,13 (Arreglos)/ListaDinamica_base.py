''' Implementación de lista dinámica '''
import ctypes

class ListaDinamica:
    def __init__(self) -> None:
        ''' Inicializar un arreglo vacío '''
        self.__n = 0                         # Elementos actuales (lista contenedora)
        self.__c = 1                         # Capacidad inicial por defecto
        self.__A = self.__init_arr(self.__c) # Arreglo contenedor

    def __len__(self) -> int:
        ''' Regresa la cantidad de elementos almacenados en la lista '''
        return self.__n

    def __getitem__(self, k) -> object:
        ''' Regresa un elemento en una posición k -> arreglo[k]; k = -1 -> arreglo[ultima_posición_valida] '''
        if k < 0:
            if abs(k) > self.__n:
                raise IndexError(f'Índice inválido ({k})')
            k = self.__n + k
        elif k >= self.__n:
            raise IndexError(f'Índice inválido ({k})')
        
        return self.__A[k]

    def append(self, obj) -> None:
        ''' Añade un elemento al final de la lista '''
        if self.__n == self.__c: # Extender la lista
            self.__resize(2 * self.__c)
        
        self.__A[self.__n] = obj
        self.__n += 1

    def __resize(self, c) -> None:
        ''' Modifica el tamaño de la lista interna '''
        B = self.__init_arr(c)

        for i in range(self.__n):
            B[i] = self.__A[i]
        
        self.__A = B
        self.__c = c

    def __init_arr(self, capacidad): # No tocar; Ya implementada
        ''' Regresa un nuevo arreglo con capacidad determinada '''
        return (capacidad * ctypes.py_object)()     # Magia

if __name__ == '__main__':
    '''
        Pruebas de la clase:
        El siguiente código no debe ser modificada
        y debe correr sin errores
    '''
    # 1. Instanciación
    ld = ListaDinamica()

    # 2. Inserción de al menos 5 elementos
    temp = [10, 20, False, -0.53, 'String', 1, 1, 1, 1, 1, 1, 1, 1]

    for i in temp:
        ld.append(i)
        print(f'Se agregó {i}\n\tCapacidad actual: {ld._ListaDinamica__c}, Elementos actuales: {len(ld)}')

    # 3. Impresión de los elementos usando for
    ''' Descomentar el siguiente for si se hizo la implementación de índices negativos '''
    for i in range(1, len(ld)+1):
        print(ld[-i])

    ''' Usar el siguiente for en caso contrario '''
    # for i in range(len(ld)):
    #     print(ld[i])
