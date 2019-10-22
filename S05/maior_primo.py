def maior_primo(num):
    i = 2
    maiorPrimo = num
    fgPrimo = True

    while i < num and fgPrimo:
        if num % i == 0:
          fgPrimo = False
        #print(i)
        i = i + 1
        if fgPrimo:
            maiorPrimo = i
        else:
            num = num - 1
            i = 2
            fgPrimo = True
    return maiorPrimo
