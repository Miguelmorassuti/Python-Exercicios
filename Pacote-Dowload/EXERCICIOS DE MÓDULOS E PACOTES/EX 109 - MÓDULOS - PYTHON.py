#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um
# parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moedatree


esc = int(input("\033[3;36mDIGITE UM VALOR:\033[m R$"))
moedatree.metade(esc)
print(f"A metade de R${moedatree.moeda(esc)} é {moedatree.metade(esc,True)}")

moedatree.dobro(esc)
print(f"O dobro de R${moedatree.moeda(esc)} é {moedatree.dobro(esc,True)}")

moedatree.aumento10(esc)
print(f"O valor R${moedatree.moeda(esc)} ao ser acrescentado 10% se torna {moedatree.aumento10(esc,True)}")