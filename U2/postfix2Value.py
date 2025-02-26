import os

def postfix2Value(postfix):
    lista = postfix.split()
    print(lista)  
    value = 10      
    return value

infix = "4-3^2/3+7*(1-2)"
postfix = "4 3 2 ^ 3 / - 7 1 2 - * +"
valor = -6

infix  = '2*(2^3*2-6/(4-2)-10)-2' 
postfix = "2 2 3 ^ 2 * 6 4 2 - / - 10 - * 2 -"
valor = 4


valor = postfix2Value(postfix)
print(valor)




