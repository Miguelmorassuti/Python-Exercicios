#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total
#de gols feitos durante o campeonato.
arma = {}
totgol = 0
gols = []

#COLETANDO DADOS
arma['JOGADOR'] = str(input("\033[1;34mNOME DO JOGADOR ==>\033[m")).upper()
partidas = int(input(f"\033[1;34mQUANTAS PARTIDAS O ATLETA {arma['JOGADOR']} DISPUTOU ==>\033[m"))
print("\033[2;35m===\033[m"*18)

#COLETANDO GOLS POR PARTIDAS, SOMANDO TOTAL E COLOCANDO NO DICIONARIO, GOLS SEPARADOS ESTÃO NUMA LISTA ADD NO DIC
for p in range(1, (partidas+1)):
    gol = int(input(f"\033[3;30mQUANTOS GOLS O JOGADOR FEZ NA {p}° PARTIDA ==>\033[m"))
    totgol+=gol
    gols.append(gol)
    arma['GOLSS'] = gols
    arma['GOLS TOTAIS'] = totgol
    print("\033[2;35m-=-\033[m"*18)

#PRINTANDO ESCOPO TOTAL
print(arma)
print("___"*18)
for k, v in arma.items():
    print(f"O CAMPO {k} POSSUI VALOR {v}")
print("___"*18)

cont_nº_partida = 1  #gambiarra para ficar bonito
#PRINTANDO GOLS POR JOGOS
name = arma['JOGADOR']
print(f"O ATLETA DISPUTOU UM TOTAL DE {partidas} PARTIDAS")
for c in arma['GOLSS']:
    print(f'    ==> NA {cont_nº_partida}ºPARTIDA O {name} FEZ {c} GOLS')