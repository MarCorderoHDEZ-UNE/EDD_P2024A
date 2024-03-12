''' Invertir un archivo '''
import sys
sys.path.append('../../../')
from Stack import Stack

def reverse_file(file, new_file) -> None:
    ''' Invierte los contenidos de un archivo '''
    S = Stack()

    with (open(file, 'r')) as f:
        for i in f.readlines():
            S.push(i)
        
        with (open(new_file, 'w')) as nf:
            while not S.is_empty():
                nf.write(S.pop())

if __name__ == '__main__':
    entrada = 'entry.txt'
    salida = 'out.txt'
    reverse_file(entrada, salida)
