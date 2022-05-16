salário = float(input("Ola companheiro, informe seu salário, iremos fazer reajustes >>"))
if salário <= 1250:
    print((f"O seu novo salário sera de:"),salário*1.15 , "Reais")
else:
    print((f"O seu salário a partir de hoje será de:"), salário*1.10 , "Reais")
