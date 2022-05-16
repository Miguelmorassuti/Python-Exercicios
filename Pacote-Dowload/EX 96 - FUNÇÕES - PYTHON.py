#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(l,c):
    a= l*c
    print(f"A AREA DE UM TERRENO COM DIMENSÕES {l} X {c} É DE {a} METROS QUADRADOS")


print("CALCULANDO AREAS")
print("-=-"*18)

l = float(input("LARGURA DO TERRENO (METROS)==>"))
c = float(input("LARGURA DO COMPRIMENTO (METROS) ==>"))

area(l,c)
