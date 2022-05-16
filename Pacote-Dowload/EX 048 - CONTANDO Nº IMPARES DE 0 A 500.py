soma = 0
cont = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
        print(n)
print(f"O SOMATÓRO DE TODOS OS ESSES VALORES FOI DE {soma}")
print(f"AO TODO FORAM CONTABLIZADOS {cont} VALORES QUE SÃO DIVISIVEIS POR 3")
