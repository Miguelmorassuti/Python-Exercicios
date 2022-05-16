print("OI AMIGO, IREI CALCULAR O SEU IMC!!")
print("=-=-"*20)
peso = float(input("DIGITE SEU PESO EM QUILOGRAMAS >>"))
altura = float(input("DIGITE SUA ALTURA >>"))
imc = peso/(altura*altura)
print(f"O SEU IMC É DE {imc:.2f}")
if imc<18.5:
    print("ABAIXO DO PESO!!")
elif imc<25.0:
    print("PESO NORMAL, AI SIM HEIN PAI!")
elif imc<=30:
    print("SOBREPESO HEIN PAI, BORA LANÇAR O PROJETINHO FELAS")
elif imc<=40:
    print("OBESO, TA GORDÃO HEIN FI")
elif imc>40:
    print("OBESIDADE MORBIDA, VAI MORRER!!!!")

