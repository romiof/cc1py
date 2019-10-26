# >>>lista = [2, 4, 2, 2, 3, 3, 1]
# >>>remove_repetidos(lista)
# [1, 2, 3, 4]
def remove_repetidos(lista):
    lista_limpa = []
    for ele in lista:
        if ele not in lista_limpa:
            lista_limpa.append(ele)

    # return sorted(lista_limpa)
    lista_limpa.sort()
    return  lista_limpa

def main():
    lista = [2, 4, 2, 2, 3, 3, 1]
    print ( remove_repetidos(lista) )

main()
