''' Evidencia empírica de arreglos dinámicos en Python '''
from sys import getsizeof

holder = []
for i in range(1000):
    a = len(holder)
    b = getsizeof(holder)

    print(f'Longitud: {a:>3}; Tamaño en bytes: {b:4d}')
    holder.append(None)
