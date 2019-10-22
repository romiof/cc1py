import math
x1 = int ( input ("Por favor, digite o x1 número inteiro: "))
x2 = int ( input ("Por favor, digite o x2 número inteiro: "))
y1 = int ( input ("Por favor, digite o y1 número inteiro: "))
y2 = int ( input ("Por favor, digite o y2 número inteiro: "))

dis = math.sqrt(((x1-x2)**2)+((y1-y2)**2))

if dis >= 10:
    print("longe")
else:
    print("perto")
