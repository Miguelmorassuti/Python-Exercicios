#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
#diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda


esc = int(input("\033[3;36mDIGITE UM VALOR:\033[m R$"))
moeda.metade(esc)
print(f"A metade de {esc} é {moeda.metade(esc)}")

moeda.dobro(esc)
print(f"O dobro de {esc} é {moeda.dobro(esc)}")

moeda.aumento10(esc)
print(f"O valor {esc} ao ser acrescentado 10% se torna {moeda.aumento10(esc)}")