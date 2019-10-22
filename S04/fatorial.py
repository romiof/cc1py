#Semana 04 EX 01
num = int(input("Digite o valor de n: "))

fat = 1

if num != 0:
  while num > 0:
    fat = fat * num
    num = num - 1

print(fat)
