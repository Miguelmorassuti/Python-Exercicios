print("=-=-=- CONTADOR DE PROGRESSÃO ARITMÉTICA -=-=-=")
pt = int(input("DIGITE O PRIMEIRO TERMO DA P.A. -->"))
razao = int(input("DIGITE A RAZÃO DA P.A. -->"))
contagem = 0
zera = False
while zera == False:
    if contagem == 0:
        print(pt, end = " ")
    else:
        pt = razao + pt
        print(pt, end= " ")
    contagem +=1
    if contagem == 10:
        zera = True
print("FIM...")