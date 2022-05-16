km = int(input("QUAL SERA A DISTANCIA DA SUA VIAGEM EM KM? >>"))
print((f"Sua viagem que será de"), km , "KM")
if km<=200:
    preço = 0.5*km
    print((f"SUA VIGEM CUSTARÁ "), preço , "reais")
else:
    custo = 0.45*km
    print((f"Sua viagem custará"), custo ,"reais")