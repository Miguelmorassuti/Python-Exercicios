#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
 print(f'Calculando {numero}! = ', end='')
 produtoFinal = 1
 for c in range(numero, 0, -1):
  if show:                                  #show true significa q show existe
   print(c, end=' x ' if c > 1 else ' = ')
  produtoFinal *= c
 return produtoFinal


print(fatorial(4, show=False))
input()