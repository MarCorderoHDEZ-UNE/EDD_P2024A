def encriptar(cadena: str) -> str:
    if (len(cadena) == 1 or not cadena):
        return cadena

    res = ""
    mitad = len(cadena) // 2

    if (len(cadena) % 2 != 0):
        res += cadena[mitad]
        res += encriptar(cadena[:mitad])
        res += encriptar(cadena[mitad + 1:])
    else:
        res += cadena[mitad - 1]
        res += encriptar(cadena[:mitad - 1])
        res += encriptar(cadena[mitad:])

    return res

def encriptar_simple(cadena: str) -> str:
    if (0 <= len(cadena) <= 1):
        return cadena

    res = ""
    mitad = len(cadena) // 2
    impar = len(cadena) % 2 != 0

    res += cadena[mitad - (0 if impar else 1)]
    res += encriptar(cadena[:mitad - (0 if impar else 1)])
    res += encriptar(cadena[mitad + (1 if impar else 0):])

    return res

print(encriptar('abcxdef'))
print(encriptar_simple('abcxdef'))
    