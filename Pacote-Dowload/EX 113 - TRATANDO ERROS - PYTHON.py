#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.

def LeiaInt(x):
    while True:
        valor = str(input(x))
        if valor.isnumeric():
            return valor
        else:
            print("\033[1;31mERRO!!!, DIGITE UM N° INTEIRO, TENTE NOVAMENTE\033[m")

def LeiaFloat(y):
        while True:
            try:
                num = float(input(y))
            except (ValueError, UnboundLocalError):
                print("\033[1;31mERRO!!!,DIGITE UM Nº REAL, TENTE NOVAMENTE\033[m")
                continue    #função que serve para fazer a função parar aq e começar td denovo
                return 0
            else:
                return num


#PROGRAMA PRINCIPAL
n = LeiaInt("DIGITE UM NÚMERO INTEIRO:")
print(f"VOCE ACABOU DE DIGITAR O N° ==> {n}")
print("-="*20)

m = LeiaFloat("DIGITE UM NÚMERO REAL:")
print(f"VOCE ACABOU DE DIGITAR O NÚMERO {m}")
