# Receba 3 números inteiros na entrada e imprima
# crescente
# se eles forem dados em ordem crescente. Caso contrário, imprima
# não está em ordem crescente */

n1 = int ( input ("Por favor, digite o 1º número inteiro: "))
n2 = int ( input ("Por favor, digite o 2º número inteiro: "))
n3 = int ( input ("Por favor, digite o 3º número inteiro: "))

if (n1 <= n2) and (n2 <= n3):
    print("crescente")
else:
    print("não está em ordem crescente")
