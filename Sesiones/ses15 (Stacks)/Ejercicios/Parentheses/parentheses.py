''' Comprobar paréntesis '''
import sys
sys.path.append('../../../')
from Stack import Stack

def check(string) -> bool:
    ''' Revisa si los paréntesis, corchetes o
        llaves de una cadena están balanceados '''
    S = Stack()
    open_p = ('(', '[', '{')
    close_p = {')': '(', ']': '[', '}': '{'}

    for s in string:
        if s in open_p:
            S.push(s)
        elif s in close_p:
            if S.is_empty():
                return False

            if close_p[s] == S.top():
                S.pop()

    return S.is_empty()

if __name__ == '__main__':
    valido = '(a + b)*(c - (20z))'
    invalido = '((a+b))*{}][30]'

    print(check(valido))
    print(check(invalido))

    otro = '(((({{{{{[[[[()]]]]}}}}})))'
    print(check(otro))
