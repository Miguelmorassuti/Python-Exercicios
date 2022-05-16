numero = int(input("DIGITE UM Nº E DIREI SE ELE É PAR OU IMPAR:"))

# O SIMBOLO DE % SERVE PARA MOSTRAR O RESTO DA DIVISÃO, TODO NºPAR O RESTO DA DIVISÃO É 0, TODO IMPAR O RESTO É 1
resultado = numero % 2
if resultado == 0:
    print("PAR")
else:
    print("IMPAR")

