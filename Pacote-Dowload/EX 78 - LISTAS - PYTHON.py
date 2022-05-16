lista = []
cont= 0
for num in range (0,5):
    cont = 1 + cont
    n = int(input("DIGITE UM NÚMERO ->"))
    lista.append(n)
    if cont == 1:
        maior = menor = n
    else:
        if n>=maior:
            maior = n
        if n<=menor:
            menor = n
print(lista)
print(f'O MAIOR NÚMERO DA LISTA É O {maior} QUE FICA NA POSIÇÃO ', end=' ')
for i, c in enumerate(lista):
    if c == maior:
        print(i ,'... ', end=' ')
print(f'\nO MENOR NÚMERO DA LISTA É O {menor} QUE FICA NA POSIÇÃO ', end=' ')
for i , c in enumerate(lista):
    if c ==menor:
        print(i, '...', end=' ')



'''print(f"O maior nº da lista é o {max(lista)}") #jeito facil de resolver usando função kk
print(f"O menor nº da lista é o {min(lista)}")'''