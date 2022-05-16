#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


import time

def contador():
    for a in range(inicio,fim,passo):
        time.sleep(1)
        print(a,end=' ')
    print(" ")
    print("-=-"*18)
    print(f"CONTAGEM DE 1 A 10")
    for p in range(1,11):
        time.sleep(1)
        print(p,end=" ")
    print("END...")
    print("-=-"*18)
    print("CONTAGEM DE 10 A 0 COM PASSO DE 2")
    for dec in range(10,-1,-2):
        time.sleep(1)
        print(dec, end=" ")
    print("END...")
    print("-=-" * 18)


print("-=-" * 18)
print("FAÇA SUA CONTAGEM PERSONALIZADA")
print("-=-" * 18)
inicio = int(input("INÍCIO ==>"))
fim = int(input("FIM ==>"))
passo = int(input("PASSO ==>"))

contador()

