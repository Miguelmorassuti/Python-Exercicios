#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = int(input('\033[1;31mQuantos jogadores você quer analisar? '))
jogador = dict()
for c in range(jogadores):
    jogador[c] = dict()
    jogador[c]["Nome"] = str(input(f'\033[1;35mNome do {c+1}º Jogador: '))
    jogador[c]["Partidas"] = int(input('Partidas jogadas: '))
    jogador[c]["Total de Gols"] = 0
    for x in range(1, jogador[c]["Partidas"]+1):
        jogador[c][f"Gols na {x}ª partida"] = int(input(f'Gols na {x}ª partida: '))
        jogador[c]["Total de Gols"] += jogador[c][f"Gols na {x}ª partida"]
    print('\033[1;33m-=' * 25)
print('\033[1;30mJogador(es): ')
for j in range(jogadores):
    print(f'\033[1;33mNúmero de identificação: {j}')
    for k, v in jogador[j].items():
        print(f'\033[1;36m{k} tem o valor: \033[1;35m({v})')
    print('\033[1;33m-=' * 25)
while True:
    Dados = int(input('\033[1;36mMostrar estatísticas de qual jogador? (999 para parar): '))
    if Dados == 999:
        print('\033[1;31mFinalizado!')
        break
    if Dados >= len(jogador):
        print(f'\033[1;31mErro! Não existe jogador com o código: {Dados}')
    else:
        print(f'\033[1;35mLevantamento do(a) jogador(a) {jogador[Dados]["Nome"]}: ')
        for x in range(1, jogador[Dados]["Partidas"] + 1):
            print(f'No jogo {x} fez {jogador[Dados][f"Gols na {x}ª partida"]} gol(s).')


