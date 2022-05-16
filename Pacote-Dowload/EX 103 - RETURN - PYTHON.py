#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def FICHA(n, x):
    if n =="":
        n = "<DESCONHECIDO>"
    if x =="":
        x = 0
    return print(f"JOGADOR ==> {n} \nGOL(S) NO CAMPEONATO ==> {x}")


#PROGRAMA PRINCIPAL:
nome_jogador = str(input("NOME DO JOGADOR ==>")).strip().title()
gols = input("GOLS FEITOS ==>").strip()
print("~~"*18)
FICHA(nome_jogador,gols)