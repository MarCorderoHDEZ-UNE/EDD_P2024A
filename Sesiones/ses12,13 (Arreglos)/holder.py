''' Parte 1 '''
pnt1 = 0
pnt2 = 0
pnt3 = 0
pnt4 = 0
pnt5 = 0

# Equivalente a ↓

pnt = [0, 0, 0, 0, 0]
pnt = [0] * 5

''' Parte 2 '''
pacientes = ['Rene', 'Hassan', 'Laija', 'Ricardo', 'Antonio']

primes = [2, 3, 5, 7, 11, 13, 17, 19]
temp = primes[3:6]
temp[2] = 15
print(f'{primes=}\n{temp=}')

backup = list(primes)
backup[0] = -999
print(f'\n{primes=}\n{backup=}')

from copy import copy
l1 = ['Marco', 'Ricardo', 'Cordero', 'Hdez']
l2 = copy(l1)
l2[3] = 'Hernández'
print(f'\n{l1=}\n{l2=}')

counters = [0] * 8
counters[2] += 1

extras = [23, 29, 31]
primes.extend(extras)

''' Parte 3 '''
from array import array
from sys import getsizeof

trad = [2, 3, 5, 7, 11, 13, 17, 19]
comp = array('i', [2, 3, 5, 7, 11, 13, 17, 19])

print(f'\n{getsizeof(trad)=}\n{getsizeof(comp)=}')

''' Parte 4 '''
arr = [10, 20, 30, 40] # len = 4
arr.append(50) # len = 5
