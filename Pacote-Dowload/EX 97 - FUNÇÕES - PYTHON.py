#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    c = len(txt) * 2
    print("~"*(len(txt)*2))         #função center centraliza o texto .center(total de caracteres)
    print(txt.center(c))
    print("~"*(len(txt)*2))


escreva("bacon")
escreva("curso em video é mo maneiro")
escreva("fnx")