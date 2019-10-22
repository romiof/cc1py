num = int(input("Digite um número para somarmos os algarismos dele: "))

soma = 0

while num > 0:
    soma = soma + (num % 10)
    num = num // 10

print("A soma dos algarismos é:",soma)