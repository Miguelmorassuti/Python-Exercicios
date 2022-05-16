#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.
L = []
pares = []
impares = []
while True:
    L.append(int(input("DIGITE UM NÚMERO ->")))
    esc = str(input("DESEJA CONTINUAR [S]/[N]? ->")).upper().strip()
    while esc[0] not in "SN":
        print("OPÇÃO INVALIDA !!!")
        esc = str(input("DESEJA CONTINUAR [S]/[N]? ->")).upper().strip()
    if esc =="S":
        print("-=-"*18)
    else:
        print(f"LISTA COMPLETA --->{L}")

        pos = 0
        for pos , i in enumerate(L):
            if i % 2 ==0:
                pares.append(i)
            elif i % 2 ==1:
                impares.append(i)

        print(f"NÚMEROS PARES ---->{pares}")
        print(f"NÚMEROS IMPARES -->{impares}")
        break

#print(*pares, sep=' ,')







