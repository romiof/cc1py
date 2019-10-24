def main():
    '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''
    fgModoJogo = False
    modoJogo = 0
    while not (fgModoJogo):
        print("Bem-vindo ao jogo do NIM! Escolha:\n")
        print("1 - para jogar uma partida isolada")
        modoJogo = input("2 - para jogar um campeonato ")
        if modoJogo == "1":
            fgModoJogo = True
            partida()
        #elif modoJogo == "2":
        #    fgModoJogo = True
        #    campeonato()
        else:
            opcInvalida()

def opcInvalida():
    print("\nOops! Jogada inválida! Tente de novo.\n")

def partida():
    #
    # Solicita M e N e vai chamando as funções anteriores.
    #
    pcsInfomradas = True
    while pcsInfomradas:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if n > m:
            pcsInfomradas = False
        else:
            print("Limite de peças retiradas por jogada deve ser menor que a Quantidade de Peças.")
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


#devolve um inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora.

def computador_escolhe_jogada(n, m):
    movPc = 0
    aux = True
    while aux:
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


#campeonato()

# uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato.
# Essa nova função deve realizar três partidas seguidas do jogo e, ao final,
# mostrar o placar dessas três partidas e indicar o vencedor do campeonato.
# O placar deve ser impresso na forma
# Placar: Você ??? X ??? Computador

main()

#computador_escolhe_jogada(5, 2)