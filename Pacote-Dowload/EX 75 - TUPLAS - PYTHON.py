n1 = int(input("DIGITE UM NÚMERO:"))
n2 = int(input("DIGITE UM NÚMERO:"))
n3 = int(input("DIGITE UM NÚMERO:"))
n4 = int(input("DIGITE UM NÚMERO:"))
tupla = n1 , n2 , n3 , n4
cont9 = contpar = 0
print(("você digitou os valores ") , tupla)
print(("Em ordem crescente -->") , sorted(tupla))
for n in tupla:
    if n == 9:
        cont9 += 1
    elif n%2 == 0:
        print(n , end=" ")
print("São números pares")
print("O nº 9 apareceu em " , (cont9) , "ocasiões") #nome da variavel.count(9)
if 4 in tupla:
    print(("o nº4 teve sua primeira aparição na posicão ") , tupla.index(4)+1)
else:
    print("O nº 4 não esta presente na tupla!!")
