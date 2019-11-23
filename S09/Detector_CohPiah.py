import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    # Devolve um Vetor
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    """ Recebe uma posição do Vetor e devolve uma Lista com as Sentenças """
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    """ A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
     ### IN: Str OUT: [f1, f2, f3, ...] """
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    # IMPLEMENTADA !
    dife = 0
    for i in range(len(as_a)-1):
        dife += abs(as_a[i] - as_b[i])
    dife /= 6
    return dife

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Recebe uma String --> separaSentença --> separaFrase --> separaPalavra --> Cálculos
    # --> return Vetor [1, 2, 3, 4, 5, 6]
    frases = []
    frasesTemp = []
    palavrasTemp = []
    palavras = []
    cont_palavrasTxt = 0
    cont_caracteresTxt = 0
    cont_caracteresSen = 0
    cont_caracteresFra = 0
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        cont_caracteresSen += len(sent)
        frasesTemp = separa_frases(sent)
        for frase in frasesTemp:
            cont_caracteresFra += len(frase)
            frases.append(frase)
            palavrasTemp = separa_palavras(frase)
            for palavra in palavrasTemp:
                palavras.append(palavra)
                cont_caracteresTxt += len(palavra)

    cont_palavrasTxt = len(palavras)
    assinatura = []
        #Tamanho médio de palavra : Média simples do número de caracteres por palavra.
    assinatura.append(cont_caracteresTxt / cont_palavrasTxt)
        #Relação Type-Token       : Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    assinatura.append(n_palavras_diferentes(palavras) / cont_palavrasTxt)
        #Razão Hapax Legomana     : Número de palavras utilizadas uma vez dividido pelo número total de palavras.
    assinatura.append(n_palavras_unicas(palavras) / cont_palavrasTxt)
        #Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    assinatura.append(cont_caracteresSen / len(sentencas))
        #Complexidade de sentença : Média simples do número de frases por sentença.
    assinatura.append(len(frases) / len(sentencas))
        #Tamanho médio de frase   : Média simples do número de caracteres por frase.
    assinatura.append(cont_caracteresFra / len(frases))

    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    notaTestes = []
    for texto in textos:
        calcAs = calcula_assinatura(texto)
        notaTestes.append(compara_assinatura(calcAs, ass_cp))
    
    posicaoTextoInfectado = 0
    i = 0
    while i < len(notaTestes):
        if notaTestes[i] < notaTestes[posicaoTextoInfectado]:
            posicaoTextoInfectado = i
        i += 1

    return posicaoTextoInfectado + 1


def main():
    # Leitura das Assinaturas
    l_assinaturas = le_assinatura()

    # Leitura dos Textos
    l_textos = le_textos()

    # Avalia os Textos
    textoInfectado = avalia_textos(l_textos, l_assinaturas)
    
    # Saída
    print("O autor do texto \033[0;31m", textoInfectado, "\033[m está infectado com COH-PIAH")



#avalia_textos(
#    [  'Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.'
#     , 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.'
#     , 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
#    ]    
#    , [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
#)

main()