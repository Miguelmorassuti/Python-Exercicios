velo = int(input("DIGITE A VELOCIDADE DO VEÍCULO >>"))
if velo<=80:
    print("TUDO OK!!! MOTORISTA NÃO COMETEU INFRAÇÃO")
else:
    multa = (velo -80)*7
    print("ALERTA!!! MOTORISTA ULTRAPASSOU O LIMITE DE VELOCIDADE")
    print((f"VOCE DEVE PAGAR UMA MULTA DE R$") , multa )
print("TENHA UM BOM DIA!")

