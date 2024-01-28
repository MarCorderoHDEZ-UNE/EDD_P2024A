# nombre_de_la_variable = []
# metodo2 = list('ABCDE')

# print(metodo2)

# for i in 'CADENA DE CARACTERES':
#     print(i)

# lista = range(100) # range(a,b,c) [a,b)
# # print(list(lista))

# for i in lista: # for i in range(100)
#     print(i)

# x = list(range(1,11,2)) # for (int i = 1; i < 10, i += 2) # n = 5

# for i in range(len(x)): # length
#     print(i, x[i])

# for i, elemento in enumerate(x):
#     print(i, elemento)

# import random

# desordenada = [random.randint(1,100) for _ in range(10)]
# print(desordenada)
# desordenada.sort(reverse=True) # nlog(n)
# print(desordenada)

otraLista = list('Marco Cordero')
otraLista.reverse()
# elemento = otraLista[0] + otraLista[1] + otraLista[3] # Mar
# elemento = otraLista[:4]
# elemento = otraLista[4:]
# otraLista.reverse()
# #elemento = otraLista[0:-4:3]
# #elemento = otraLista[::-1]
# print(otraLista)

# holder = ''
# for i in range(len(otraLista)):
#     holder = otraLista[i] + holder
# print(holder)

# elemento_volteado = ''.join(list(reversed(elemento)))
# print(elemento_volteado)

# lista = list(range(10))
# print(lista[len(lista)-1])
# print(lista)
# holder = lista.pop()
# print(holder)
# print(lista)

# listavacia = []
# for i in range(50):
#     listavacia.append(i+1)
# print(listavacia)

x = [0,1,2,3,1,4,0]
# x.insert(18,True)
print(x[-8])
