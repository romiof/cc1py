# Listas, são similares a vetores e arrays.
# 
# Começam a contar do ZERO os elemtnos
# 
frutas_list = ["Maça", "Banana", "Bergamota", "Melancia"]

# Retornar primeiro elemento da lista
frutas_list[0]

# Retornar o último elemento da lista
# O sinal negativo retorna contando de trás pra frente
frutas_list[-1]


# LEN retorna a quantidade de elementos de uma lista
# LEN também retorna o tamanho de variáveis que são STRINGS
len(frutas_list)

# Listas podem ter diversos tipos de objetos dentro delas.
filmes = ["Era uma vez no oeste", 1968, 3.9, "John Travolta"]

type(filmes)
type(filmes[0])
type(filmes[1])
type(filmes[2])


# Acrescentar novos elementos a uma lista.
# Usar a função APPEND para adicionar o elemento no final da lista.
frutas_list.append("Laranja")

# Atribuir valores para as posições da lista, substituíndo o valor atual.
frutas_list[3] = "Pera"

#
# DESAFIO:  Faça programa que vai lendo do teclado uma sequência de números inteiros terminadas por zero e quando o usuário digita o zero, ele imprimi essa sequência na ordem inversa.
# Na ordem ao contrário da ordem que o usuário digitou.
#

i = 1
lista = []
while i != 0:
    i = int(input("Informe números para a lista. Zero para sair: "))
    if i != 0:
        lista.append(i)
i = len(lista) - 1
while i >= 0:
    print(lista[i], end=" ")
    i = i - 1

# 
# FOR, usado para passar pelos elementos das listas
# 
frutas_exoticas = ["Jaca", "Gavirola", "Jabuticaba"]
for fruta in frutas_exoticas:
    print ("Eu adoro", fruta)

# 
# RANGE, é um objeto que cria um intervalo de valores
# range(20) --> Cria um objeto que vai ter 20 posições... MAS ELE VAI IR DO 0 à 19
# 
for i in range(20):
    # Vai do ZERO à 19

for i in range(5, 20):
    # Vai do CINCO à 19

for i in range(5, 20, 3):
    # Vai do CINCO à 19 --> passo de 3 em 3 (pula de 3 em 3)


#
# Manipulação de listas
#
# Fatias de listas. Retorna a range das posições.
# Nesse exemplo, vai da posição 2 até a 5. Não considera o último elemento.
frutas_list[2:6]

# Posição 3 até o final da lista:
frutas_list[3:] 

# Posição 0 até a posição 9:
frutas_list[:10]

#
# CLONANDO LISTAS.
#
# Ao atirbuir uma lista para outra, o Python vai mapear a nova variável para a mesma lista
# Assim, ao alterar elemtendos de uma lista, ambas serão alteradas.
# Para contornar isso, é necessário CLONAR a lista para uma nova:
# Simplesmente fazer assim:
frutas2 = frutas_list[:]
# Também seria possível criar uma lista[] , e atráves de uma função de for-loop na lista principal, fazer append dos elemntos.
# Mas não vale a pena, visto que o hack acima resolve o problema.

#
# PERTINÊNCIA DE ELEMENTOS EM LISTAS.
#
cores = ["Vermelho", "Azul", "Verde"]
"Azul" in cores
# Resposta é True

#
# CONCATENAÇÃO DE LISTAS.
# Diferente do Append, a concatenção não altera a lista existente
numeros = [1, 2, 3] + [4, 5, 6]

a = ['a', 'b', 'c']
b = ['z', 'x', 'y']
print(a + b)
# ['a', 'b', 'c', 'z', 'x', 'y']

#
# REPETIÇÃO DE LISTAS.
# 
a = ['a', 'b', 'c']
a_triplicado = a * 3
print(a_triplicado)
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

#
# REMOÇÃO DE ELEMENTOS EM LISTAS.
# 
a = ['a', 'b', 'c']
del a[1]
print(a)
# ['a', 'c']

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del a[1:5]
print(a)
# ['a', 'f', 'g']

