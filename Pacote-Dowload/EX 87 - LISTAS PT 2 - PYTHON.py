#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.  B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

print("\033[1;34m MATRIZ 3X3 v2.0 \033[m")
print("-="*30)
num = [[], [], [], [], [], [], [], [], []]
par = 0
for pos in range(0,9):
    n = int(input(f"DIGITE O {pos+1}º NÚMERO ->"))
    num[pos].append(n)

#SOMANDO PARES
    if n % 2 ==0:
        par += n

print(num[0],  num[1],  num[2])
print(num[3],  num[4],  num[5])
print(num[6],  num[7],  num[8])
print(f"\033[1;31m A SOMA DE TODOS OS NÚMEROS PARES É {par} \033[m")
print(f"\033[1;33m A SOMA DOS NUMEROS DA TERCEIRA COLUNA É {sum(num[2] + num[5]+ num[8])} \033[m") #SUM soma itens de uma lista
print(f"\033[1;32m O MAIOR VALOR DA SEGUNDA LINHA É {max(num[3], num[4], num[5])} \033[m")

