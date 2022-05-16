#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

L = []
for num in range (0,4):
    n = int(input("DIGITE UM NÚMERO -->"))
    if num == 0:
        L.append(n)
        print("VALOR ADICIONADO NO FIM DA LISTA COM SUCESSO...")
        n1 =n
    elif num == 1:
        n2 = n
        if n1 > n:
            L.insert(0, n)
            print("VALOR ADICIONADO NA POSIÇÃO [1]")
        else:
            L.append(n)
            print("VALOR ADICIONADO NO FIM DA LISTA COM SUCESSO...")
    elif num == 2:
        n3 = n
        if n > n1 and n > n2:
            L.append(n)
            print("VALOR ADICIONADO NO FIM DA LISTA COM SUCESSO...")
        elif (n > n1 and n <n2) or (n<n1 and n>n2):
            L.insert(1, n)
            print("VALOR ADICIONADO NA POSIÇÃO [2]")
        else:
            L.insert(0, n)
            print("VALOR ADICIONADO NA POSIÇÃO [1]")
    elif num == 3:
        n4 = n
        if n > n1 and n>n2 and n>n3:
            L.append(n)
            print("VALOR ADICIONADO NO FIM DA LISTA COM SUCESSO...")
        elif n < n1 and n< n2 and n< n3:
            L.insert(0, n)
            print("VALOR ADICIONADO NA POSIÇÃO [1]")
        elif (n > n1 and n <n2 and n <n3) or  (n < n1 and n >n2 and n <n3) or (n < n1 and n <n2 and n >n3):
            L.insert(1, n)
            print("VALOR ADICIONADO NA POSIÇÃO [2]")
        elif (n > n1 and n > n2 and n < n3) or (n < n1 and n > n2 and n > n3) or (n> n1 and n < n2 and n > n3):
            L.insert(2, n)
            print("VALOR ADICIONADO NA POSIÇÃO [3]")
        else:
            L.append(n)
            print("VALOR ADICIONADO NO FIM DA LISTA COM SUCESSO...")
print(L)

#maneira correta
lista = []
for c in range(5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:             #caso for o primeiro nº ou maior que o ultimo da lsta
        lista.append(n)
    else:
        for pos, x in enumerate(lista):     #se for nº do meio
            if n <= x:
                lista.insert(pos, n)
                break
print(lista)
