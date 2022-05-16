#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO OPCIONAL e OBRIGATÓRIO nas eleições.

print("\033[1;31mVOCÊ PODE VOTAR? A Inteligencia Artificial A BAIXO TE RESPONDE\033[m")
print("-=-"*18)

def VOTO(x=0):
    from datetime import date #EXISTE ESCOPO(LOCAL) PARA BIBLIOTECA, DENTRO DA FUNÇÃO OCUPA MENOS MEMÓRIA DO CPU
    idade = date.today().year - ano
    if 65>idade >18:
        return print(f'VOTO OBRIGATÓRIO, IDADE DO INDIVDUO É DE {idade}')
    elif 65<idade or 18>idade>16 :
        return print(f"VOTO OPCIONAL, IDADE DO INDIVDUO É DE {idade}")
    elif idade<16:
        return print(f'VOTO NEGADO, IDADE DO INDIVIDUO É DE {idade}')

#PROGRAMA PRINCIPAL
ano = int(input("ANO DE SEU NASCIMENTO:"))
VOTO(ano)
