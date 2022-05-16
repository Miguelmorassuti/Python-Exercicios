import random
from time import sleep
print('-=-=-=-=-=-=-=BEM VINDO AO JOKEMPYTHON-=-=-=-=-=-=-=-=')
print(" ")
print("FAÇA SUA ESCOLHA, DIGITE:")
print("[1] PARA PEDRA")
print("[2] PARA PAPEL")
print("[3] PARA TESOURA")
esc = int(input("SUA ESCOLHA FOI >>"))
lista = ('papel' , 'pedra' , 'tesoura')
pc = random.choice(lista)
print("JO")
sleep (1)
print("KEN")
sleep(1)
print("PO")
sleep (1)
print('-=-='*12)
if esc == 1 and pc == 'papel':
    print("PC ESCOLHE PAPEL")
    print("GANHEI SEU PATO KKKKKK")
elif esc == 1 and pc == 'pedra':
    print("PC ESCOLHE PEDRA")
    print("EMPATAMOS")
elif esc == 1 and pc == 'tesoura':
    print("PC ESCOLHE TESOURA")
    print("VOCÊ GANHOU,  F")
elif esc == 2 and pc == 'pedra':
    print("PC ESCOLHE PEDRA")
    print("PERDI, F")
elif esc == 2 and pc == 'papel':
    print("PC ESCOLHE PAPEL")
    print("DEU EMPATE, NICE!")
elif esc == 2 and pc == 'tesoura':
    print("PC ESCOLHE TESOURA")
    print("GANHEI HAHAHAHHA, PATO")
elif esc ==3 and pc == 'papel':
    print("PC ESCOLHE PAPEL")
    print("PERDI, DROGA, F")
elif esc == 3 and pc == 'pedra':
    print("PC ESCOLHE PEDRA")
    print("GANHEI SEU TROUXA HAHAHHAHA ")
elif esc == 3 and pc == 'tesoura':
    print("PC ESCOLHE TESOURA")
    print('EMPATAMOS, AI SIMMM')