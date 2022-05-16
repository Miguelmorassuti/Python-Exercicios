#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

import random
import time
import operator
cont = 0

dic = {}
for c in range (1,5):
    dic[f"jogador {c}"]=random.randint(1,6)   #dessa forma é possivel declarar diversas variaveis com for

print("VALORES SORTEADOS")

for k,v in dic.items():
    print(f" O {k} ==> TIROU O VALOR {v} NO DADO")
    time.sleep(0.5)

    # TENTANDO FAZER A PORRA DO RANKING
print("\nRANKING\n")
for jogado, valor in sorted(dic.items(),key=operator.itemgetter(1), reverse=True): #REVERSE=TRUE deixa decrescente
    cont +=1
    print(f"{cont}º LUGAR ==> {jogado} TIROU O Nº {valor} NO DADO")

                                                        # função operator itemgetter
                                                        #serve para organizar a lista de forma crescente
                                                         # ou decrescente analisando os valores nela..
                 #

