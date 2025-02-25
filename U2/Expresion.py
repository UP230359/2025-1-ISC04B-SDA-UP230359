infix = '5 * ( 6 + 2 ) - 12 / 4'
infix = '1 / ( x + 1 / ( x + 1 / ( x + 1 / x ) ) )'
infix = '( ( -8 ) ^ 2 - 4 * 1 * 15 ) ^ ( 0.5 )'
infix = '2 ^ 4 / ( 4 * 1 ) + log ( 11 - 9 ) ^ 2'  
infix = '( -8 + ( 8 ^ 2 - 4 * 1 * 15 ) ) / ( 2 * 1 )'
infix = 'sin ( 45 ) ^ 2 + cos ( 45 ) ^ 2'
infix = 'log ( 100 ) / log ( 10 )'
infix = 'alog ( 2 ) / alog ( 1 )'


# --------------------------------------------------------
infix = 'sin ( 45 ) ^ 2 + cos ( 45 ) ^ 2'

expresion = infix.replace(" ", "")
lista = infix.split()

print(expresion)
print(lista)
