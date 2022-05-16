print("-=-=-"*16)
print("ANALISANDO TRIÂNGULOS")
print("-=-=-"*15)
lado1 = float(input("DIGITE O LADO DO PRIMEIRO SEGMENTO >>"))
lado2 = float(input("DIGITE O LADO DO SEGUNDO SEGMENTO >>"))
lado3 = float(input("DIGITE O LADO DO TERCEIRO SEGMENTO >>"))
if lado1+lado2>lado3 and lado3+lado2>lado1 and lado3+lado1>lado2:
    print("Esses segmentos são capazes de formar um triângulo")
else:
    print("Não é possivel fazer um triângulo com a medida desses segmentos!!!")

