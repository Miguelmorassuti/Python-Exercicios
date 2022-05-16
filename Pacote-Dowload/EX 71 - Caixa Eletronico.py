print("CAIXA ELETRONICO")
print("-=-"*18)
saque = int(input("DIGITE O VALOR A SER SACADO >"))
while True:
    nota50 = saque//50
    print(f"{nota50} Notas de R$50")
    saque = saque - (nota50*50)
    if saque == 0:
        break
    nota20 = saque//20
    print(f"{nota20} Notas de R$20")
    saque = saque - (nota20*20)
    if saque == 0:
        break
    nota10 = saque//10
    print(f"{nota10} Notas de R$10")
    saque = saque - (nota10*10)
    if saque == 0:
        break
    moeda1 = saque
    print(f"{moeda1} moedas de R$1,00")
    saque = saque - moeda1
    if saque == 0:
        break

