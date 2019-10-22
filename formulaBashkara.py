# A, B ,c
# deta < 0 não tem raiz  ||| delta = 0 tem uma raiz ||| delta > 0 tem 2 raizs

import math

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

delta = (b**2) - (4 * a * c)
if delta < 0:
    print("Delta MENOR que zero, impossível calcular a fórmula.")
else:
    if delta == 0:
        x = ((- b) + math.sqrt(delta)) / (2 * a)
        print("Delta IGUAL à zero, X é igual à:", x)
    else:
        x1 = ((- b) + math.sqrt(delta)) / (2 * a)
        x2 = ((- b) - math.sqrt(delta)) / (2 * a)
        print("Delta MAIOR que zero, X1 é igual à:", x1, "X2 é igual à:", x2)
print("\n FIM!")
