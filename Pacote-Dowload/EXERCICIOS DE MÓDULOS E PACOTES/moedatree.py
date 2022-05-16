#MODULO - EX 109

def metade(preço,formato=False):
    res = preço/2
    return res is formato if False else moeda(res)

def dobro(preço,formato=False):
    res = preço*2
    return res is formato if False else moeda(res)

def aumento10(preço,formato=False):
    res = ((preço/100)*10) + preço
    return res if formato is False else moeda(res)

def moeda(preço=0, moeda="R$"):
    return f"{moeda}{preço:.2f}".replace('.',',')