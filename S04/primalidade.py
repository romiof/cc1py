#Semana 04 EX 04
num = int(input("Digite um número inteiro: "))

primo = True
i = 2

while i < num and primo:
    if num % i == 0:
      primo = False
    i = i + 1

if primo:
  print("primo")
else:
  print("não primo")
