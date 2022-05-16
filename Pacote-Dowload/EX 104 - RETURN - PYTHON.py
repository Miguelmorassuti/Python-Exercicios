#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def LeiaInt(x):
    while True:
        valor = str(input(x))
        if valor.isnumeric():
            return valor
        else:
            print("\033[1;31mERRO!!!, TENTE NOVAMENTE\033[m")


#PROGRAMA PRINCIPAL
n = LeiaInt("DIGITE UM NÚMERO:")
print(f"VOCE ACABOU DE DIGITAR O N° ==> {n}")
