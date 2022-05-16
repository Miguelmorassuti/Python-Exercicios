print("-=-=-==-=-=-=-=LOJAS MORASSUTI-=-=-=-=-=-=-=-")
valor = float(input("Qual foi o valor total da sua compra? R$"))
print("Qual forma de pagamento você deseja utilizar?")
print("[1] à vista no dinheiro e cheque")
print("[2] à vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
opc = int(input("Digite a forma em que você realizará o pagamento >>"))
if opc ==1:
    print(f"Sua compra com os devidos reajustes da forma de pagamento custará R${valor -((valor/100)*10)}")
elif opc ==2:
    print(f"Sua compra com os devidos reajustes da forma de pagamento custará R${valor - ((valor / 100) * 5)}")
elif opc ==3:
    print(f"Sua compra custará R${valor}")
elif opc ==4:
    print(f"Sua compra com os devidos reajustes da forma de pagamento custará R${valor +((valor/100)*20)}")
