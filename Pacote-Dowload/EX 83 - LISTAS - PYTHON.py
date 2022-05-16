#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use
#parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
#na ordem correta.
lista = []
expressao = input('Digite a expressão:')
contab = contfe = 0
for c in expressao:
    if c == '(':
        contab += 1
    elif c == ')':
        contfe +=1

if contab == contfe:
    print('Essa expressão é valida!')
else:
    print('Essa expressão é inválida!')

