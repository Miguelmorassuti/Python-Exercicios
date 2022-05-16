pa = int(input("Digite o nº do primeiro termo de sua P.A. >>"))
razao = int(input("Digite a razão quer você quer sobre sua P.A. >"))
dec = pa + ((10-1) *razao)
for num in range(pa, dec + razao, razao):
    print(num, end= ' -> ')
print('ACABOU')
