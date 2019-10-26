# Programa para leitura de dois números, e impressão da área.
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
waxu = 0
haux = 0

while haux < altura:
    while waxu < largura:
        print ("#", end="")
        waxu = waxu + 1
    haux = haux + 1
    waxu = 0
    print("")