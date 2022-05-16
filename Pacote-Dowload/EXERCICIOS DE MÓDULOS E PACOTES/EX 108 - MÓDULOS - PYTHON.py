#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import moedatwo


esc = int(input("\033[3;36mDIGITE UM VALOR:\033[m R$"))
moedatwo.metade(esc)
print(f"A metade de R${esc} é {moedatwo.metade(esc)}")

moedatwo.dobro(esc)
print(f"O dobro de R${esc} é {moedatwo.dobro(esc)}")

moedatwo.aumento10(esc)
print(f"O valor R${esc} ao ser acrescentado 10% se torna {moedatwo.aumento10(esc)}")