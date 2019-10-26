# Contador de números primos entre 2 números (Min = 2 , Máx = X)
def n_primos(n):
    cont = 1
    i = 3 # comeca em 3 pois o i==2 é sempre primo, e já contabilizado no CONT == 1
    while i <= n:
        if e_primo(i):
            cont = cont + 1
        i = i + 1
    return cont
    
def e_primo(n):
    i = 2
    primo = True
    while i < n and primo:
        if n % i == 0:
            primo = False
        i = i + 1
    return primo

n_primos(10)