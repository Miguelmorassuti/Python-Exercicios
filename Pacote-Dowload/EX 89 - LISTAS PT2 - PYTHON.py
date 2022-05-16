#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
#em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
#possa mostrar as notas de cada aluno individualmente.

listao = []
while True:
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a nota do aluno: '))
    nota2 = float(input('Digite a nota do aluno: '))
    media = (nota1 + nota2) / 2
    listao.append([aluno, nota1, nota2, media])
    perg = input('Quer continuar? [S/N] ')
    if perg in 'Nn':
        break
for u in listao:
    print(f'{u[0]}: {u[3]}')

while True:
    notai = input('Quer saber as notas individuais de que aluno? [N p/ parar]')
    if notai in 'Nn':
        break
    for u in listao:
        if notai in u[0]:
            print(f'{u[0]}: {u[1]} e {u[2]}')