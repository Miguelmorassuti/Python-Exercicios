#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
#em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
#em ordem crescente.

num = [],[]
for i in range(1,8):
    n = int(input(F"DIGITE O {i}º NÚMERO:"))
    if n %2==0:
        num[0].append(n)
    else:
        num[1].append(n)
print(F"NÚMEROS IMPARES ->{sorted(num[1])}")
print(F"NÚMEROS PARES --->{sorted(num[0])}")