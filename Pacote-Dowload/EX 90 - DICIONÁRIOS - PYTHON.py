#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunomedia = {}

#coletando dados
alunomedia['nome'] = str(input("NOME DO ALUNO:"))
alunomedia['media'] = float(input("MÉDIA DO ALUNO:"))

#analisando situação
if alunomedia['media'] >= 6:
    alunomedia['resultado'] = "APROVADO"
else: alunomedia['resultado'] = "REPROVADO"

#printando resultados
print("-=-"*18)
print("ALUNO:" ,alunomedia['nome'])
print("NOTA:", alunomedia['media'])
print("SITUAÇÃO:", alunomedia['resultado'])


