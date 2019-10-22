num = int(input("Digite um número inteiro: "))

pAtual = 88888888
pAnt = 99999999
acho = False

while num > 0 and not (acho):
    #print("Entrei no while")
    pAnt = pAtual
    pAtual = num % 10
    num = num // 10
    if pAnt == pAtual:
        acho = True
        print("sim")

if pAnt != pAtual:
    print("não")
