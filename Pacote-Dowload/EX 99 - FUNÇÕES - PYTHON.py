#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

import random

def mostralinha():
    print("-=-"*18)

def maior(*num):

 #PRIMEIRO BLOCO
    maior_valor_1 = 0                      #variaveis utilizadas na função devem ser declaradas dentro da mesma
    for c in range(1,random.randint(2,20)):
        maior_1 = (random.randint(1,200))
        print(maior_1,end=' ')
        if maior_1 > maior_valor_1:
            maior_valor_1 = maior_1


    print(f"\nFORAM INFORMADOS {c} VALORES")
    print(f"O MAIOR VALOR DESSE CONJUNTO É {maior_valor_1}")
    print(" ")
    mostralinha()

#SEGUNDO BLOCO
    maior_valor_2 = 0
    for p in range(1,random.randint(2,20)):
        maior_2 = random.randint(1,200)
        print(maior_2, end=' ')
        if maior_2 > maior_valor_2:
            maior_valor_2 = maior_2

    print(f"\nFORAM INFORMADOS {p} VALORES")
    print(f"O MAIOR VALOR DESSE CONJUNTO É {maior_valor_2}")
    print(" ")
    mostralinha()

#TERCEIRO BLOCO
    maior_valor_3 = 0
    for d in range(1,random.randint(2,20)):
        maior_3=random.randint(1,200)
        print(maior_3,end=' ')
        if maior_3>maior_valor_3:
            maior_valor_3=maior_3

    print(f"\nFORAM INFORMADOS {d} VALORES")
    print(f"O MAIOR VALOR DESSE CONJUNTO É {maior_valor_3}")

maior()

