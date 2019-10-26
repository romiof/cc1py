# Invertendo a sequência de uma lista
i = 1
lista = []
while i != 0:
    i = int(input("Informe números para a lista. Zero para sair: "))
    if i != 0:
        lista.append(i)
i = len(lista) - 1
while i >= 0:
    print(lista[i])
    i = i - 1