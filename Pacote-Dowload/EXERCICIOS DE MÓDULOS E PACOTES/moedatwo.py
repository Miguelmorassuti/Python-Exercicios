#MODULO - EX 108

def metade(x):
    f = x/2
    return f"R${f:.2f}".replace(".", ",")

def dobro(y):
    g = y*2
    return f"R${g:.2f}".replace(".", ",")

def aumento10(z):
    n = ((z/100)*10) + z
    return f"R${n:.2f}".replace(".", ",")