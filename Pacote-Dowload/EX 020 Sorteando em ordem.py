import random
g1 = str(input("Digite o lider do primeiro grupo >>"))
g2 = str(input("Digite o lider do segundo grupo >>"))
g3 = str(input("Digite o lider do terceiro grupo >>"))
g4 = str(input("Digite o lider do quarto grupo >>"))
lista = [g1, g2, g3, g4]
ordem = random.shuffle (lista)
print(f" A ordem das apresentações será de:")
print(lista)
