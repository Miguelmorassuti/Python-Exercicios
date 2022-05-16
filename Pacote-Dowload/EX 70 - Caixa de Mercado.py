print('-=-'*18)
print('SIMULAÇÃO DE CAIXA DE SUPERMERCADO')
print('-=-'*18)
total = maisde100 = 0
menorvalor = 9999999
nomebarato = " "
while True:
    produto = str(input("NOME DO PRODUTO >>"))
    valor = float(input("VALOR DO PRODUTO >>"))
    if valor<menorvalor:
        menorvalor = valor
        nomebarato = produto
    total += valor
    if valor>100:
        maisde100 +=1
    print("-=-"*18)
    add = str(input("DESEJA ADICIONAR MAIS UM PRODUTO? [S/N] >>")).upper().strip()[0]
    if add == 'N':
        break
print("-=-"*18)
print(f"Ao todo essa compra custara {total}, sendo que {maisde100} produtos custam mais do que R$100,00")
print(f"O produto mais barato é o {nomebarato} que custa R${menorvalor}")

