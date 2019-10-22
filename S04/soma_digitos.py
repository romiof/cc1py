#Semana 04 EX 02
num = int(input("Digite um número inteiro: "))

soma = 0

while num > 0:
    soma = soma + (num % 10)
    num = num // 10

print(soma)
