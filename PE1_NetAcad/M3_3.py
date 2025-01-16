# Logic and bit operations
# and conjuction  ^
# or  disjunction v

# Morgan's laws.
# The negation of a conjunction is the disjunction of the negations.
# The negation of a disjunction is the conjunction of the negations.

# Bitwise operators
# & (ampersand) ‒ bitwise conjunction;
# | (bar)       ‒ bitwise disjunction;
# ~ (tilde)     ‒ bitwise negation;
# ^ (caret)     ‒ bitwise exclusive or (xor).

i = 34
j = 22
bits = i & j
print("and: ", bits)

numero = -5
print(f"1 El número {numero} en binario con signo es: {bin(numero)}")
print(f"2 El número {numero} en binario sin signo es: {bin(numero & 0xFF)}")

num_bits = 8  # Número de bits que deseas mostrar
binario_sin_signo = format(numero & (2**num_bits - 1), f'0{num_bits}b')
print(f"3 El número {numero} en binario sin signo es: {binario_sin_signo}")
print(f"4 El número {numero} en complementos a 2 es : {bin(~numero+1 & (2**num_bits - 1))}")


# binary left/right shift  
print(i>>1) # divide   by 2    2^1   i // 2
print(i<<3) # multiply by 8    2^3


