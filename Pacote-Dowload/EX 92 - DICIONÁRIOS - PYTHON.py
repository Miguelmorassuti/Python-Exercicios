#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.
#30 anos de contribuição foram utiliziados como base para elaborar a possivel data de aposentadoria
import datetime

dados = {}

dados['NOME'] = str(input("DIGITE SEU NOME:"))
nasc = int(input("ANO DE NASCIMENTO:"))
dados['IDADE'] = ((datetime.datetime.now().year)-nasc)
dados['CARTEIRA DE TRAB.'] = int(input("Nº DA CARTEIRA DE TRABALHO (DIGITE 333 SE NÃO TIVER:"))
if dados['CARTEIRA DE TRAB.'] !=333:
    dados['ANO DA CONTRATAÇÃO'] = int(input("ANO DE CONTRATAÇÃO:"))
    dados['SALÁRIO'] = float(input("SEU SALÁRIO:"))
    dados['IDADE DE APOSENTADORIA'] =(dados['ANO DA CONTRATAÇÃO']+30)-nasc
elif dados['CARTEIRA DE TRAB.'] == 333:
    del dados['CARTEIRA DE TRAB.']

print("-=-"*18)
for v, k in dados.items():
    print(f" {v} CORRESPONDE A {k}")

