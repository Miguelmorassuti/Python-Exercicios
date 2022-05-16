soma = 0
resu = 0
for par in range (1,7):
    num = int(input("Digite algum nº:"))
    if num %2 == 0:
            soma += num
            resu += 1

print(f'A soma entre os valores pares digitados é de {soma}')
print(f'Existem {resu} números pares')