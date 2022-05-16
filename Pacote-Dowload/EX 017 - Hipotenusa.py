op = float(input("Digite o valor do cateto oposto >>"))
ad = float(input("Digite o valor do cateto adjacente >>"))
hipo = ((op ** 2) + (ad ** 2)) ** (1/2)
print(f"O valor da hipotenusa será de >> {hipo:.2f}")
