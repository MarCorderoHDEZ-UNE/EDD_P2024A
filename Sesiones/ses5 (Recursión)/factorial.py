def fact(n: int) -> int:
    if (n == 1):
        return 1

    return n * fact(n - 1)

n = int(input('Ingresa el término de la sucesión: '))
print(fact(n))