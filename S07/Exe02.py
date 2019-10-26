# Programa para leitura de dois números, e impressão da área, com interior em branco.
def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    waxu = 1
    haux = 1

    while haux <= altura:
        while waxu <= largura:
            if haux == 1 or haux == altura:
                imp()
            elif waxu == 1 or waxu == largura:
                imp()
            else:
                nimp()
            waxu = waxu + 1
        haux = haux + 1
        waxu = 1
        print("")

def imp():
    print("#", end="")

def nimp():
    print(" ", end="")

main()
