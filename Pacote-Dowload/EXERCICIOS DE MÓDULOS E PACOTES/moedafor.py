#MODULO - EX 110

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

def resumo(val, aum, dim):
    res = val
    dobro = val*2
    metade = val/2
    aumento = ((val/100)*aum) +val
    diminuicao = val - ((val/100)*dim)

    print('~~'*30)
    return print(f"O VALOR DESCRITO É R${res:.2f}" 
           f"\nO DOBRO DE R${res} É R${dobro:.2f}" 
           f"\nA METADE DE R${res} é R${metade:.2f}" 
           f"\nAUMENTANDO R${aum}% A R${res} OBTEM-SE O VALOR DE R${aumento:.2f}" 
           f"\nDIMINUINDO R${dim}% A R${res} OBTEM-SE O VALOR DE R${diminuicao:.2f}")





