#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

#PRIMEIRA FUNÇÃO, SORTEANDO 5 NÚMEROS ALEATÓRIOS
from random import randint

lista_num = [randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20)]

def NUMEROS():
        print(lista_num)


#SEGUNDA FUNÇÃO, SOMANDO PARES
def SOMA():
    par = []
    pares =0
    for c in lista_num:
        if c %2 ==0:
            par.append(c)
            pares = pares+c
    print(f"A SOMA DOS NÚMEROS PARES {par} É IGUAL A ==> {pares}")


NUMEROS()
SOMA()