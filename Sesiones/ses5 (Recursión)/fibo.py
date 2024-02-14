terminos = []

def fib(n: int) -> int:
    res = None

    if n <= 1:
       res = n
    else:
       res = fib(n-1) + fib(n-2)

    return res

n = int(input('Ingresa el término de la sucesión: '))

for i in range(n):
    terminos.append(fib(i))

print(terminos)
