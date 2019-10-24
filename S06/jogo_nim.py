#
# Jogo MIN contra o PC.
# Escolher entre jogar (1) partida ou (2) campeonato.
# Defina Quantidade de Peças (N) e a Quantidade a ser Retirada (M)
# Programado para sempre o PC sempre vencer
#
def main():
    fgModoJogo = True
    modoJogo = 0
    while fgModoJogo:
        print("Bem-vindo ao jogo do NIM! Escolha:\n")
        print("1 - para jogar uma partida isolada")
        modoJogo = input("2 - para jogar um campeonato ")
        if modoJogo == "1":
            fgModoJogo = False
            partida()
        elif modoJogo == "2":
            fgModoJogo = False
            campeonato()
        else:
            opcInvalida()

def opcInvalida():
    print("\nOops! Jogada inválida! Tente de novo.\n")

def partida():
    #
    # Solicita M e N e vai chamando as funções anteriores.
    #
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    ### Começa o jogo, com um Indicador de Passagem para controlar de quem é a vez de jogar
    pcJoga = True
    if n % (m + 1) == 0:
        print("\nVoce começa!\n")
        pcJoga = False
    else:
        print("\nComputador começa!")
    while n > 0:
        if pcJoga:
            n -= computador_escolhe_jogada(n, m)
            pcJoga = False
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.\n")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            n -= usuario_escolhe_jogada(n, m)
            pcJoga = True
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.\n")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
    if pcJoga:
        print("Fim do jogo! Você ganhou!")
    else:
        print("Fim do jogo! O computador ganhou!")

def computador_escolhe_jogada(n, m):
    movPc = 0
    aux = True
    while movPc < m and aux:
        movPc = movPc + 1
        if (n - movPc) % (m + 1) == 0:
            aux = False
        elif movPc == n:
            aux = False
    if movPc > 1:
        print("O computador tirou", movPc, "peças.")
    else:
        print("O computador tirou uma peça.")
    return movPc

def usuario_escolhe_jogada(n, m):
    tiraPcs = True
    while tiraPcs:
        movPc = int(input("Quantas peças você vai tirar? "))
        if movPc <= m and movPc <= n and movPc > 0:
            if movPc > 1:
                print("\nVocê tirou", movPc, "peças.")
            else:
                print("\nVocê tirou uma peça.")
            tiraPcs = False
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")
    return movPc

def campeonato():
    contCamp = 0
    print("\nVoce escolheu um campeonato!\n")
    while contCamp < 3:
        contCamp = contCamp + 1
        print("**** Rodada", contCamp,"****\n")
        partida()
    print("\n**** Final do campeonato! ****\nPlacar: Você 0 X 3 Computador")

#
# Chamada para execução do programa
#
main()
