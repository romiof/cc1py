import math

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

delta = (b**2) - (4 * a * c)
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        x = ((- b) + math.sqrt(delta)) / (2 * a)
        print("a raiz desta equação é", x)
    else:
        x1 = ((- b) + math.sqrt(delta)) / (2 * a)
        x2 = ((- b) - math.sqrt(delta)) / (2 * a)
        if x1 <= x2:
            print("as raízes da equação são", x1, "e",x2)
        else:
            print("as raízes da equação são", x2, "e",x1)
