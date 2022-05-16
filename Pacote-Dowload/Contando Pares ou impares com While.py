cont = 'S'
par = impar = 0
while cont == 'S':
    num = int(input('WRITE A NUMBER > '))
    if num != 0:
        if num %2 == 0:
            par += 1
        else:
            impar +=1
    cont = str(input("CONTINUAR? [S] se sim ou [N] se não >>")).upper()
print('END')
print(f"Ao todo foram digitados {par} numeros pares e {impar} numeros impares ")
