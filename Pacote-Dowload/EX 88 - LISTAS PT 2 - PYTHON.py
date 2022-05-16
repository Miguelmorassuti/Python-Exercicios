#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
#para cada jogo, cadastrando tudo em uma lista composta.

import random
import time

print("\033[1;31m-=-\033[m"*10)
print("\033[1;34mSIMULADOR DA MEGA DA VIRADA\033[m")
print("\033[1;31m-=-\033[m"*10)

l = []
esc= int(input("\033[1;34mQUANTOS JOGOS SERÃO REALIZADOS:\033[m"))
for i in range(0,esc):
    time.sleep(0.5)
    n1 = random.randint(1, 60)
    n2 = random.randint(1, 60)
    n3 = random.randint(1, 60)
    n4 = random.randint(1, 60)
    n5 = random.randint(1, 60)
    n6 = random.randint(1, 60)
    l = [[n1], [n2], [n3], [n4], [n5], [n6]]
    print(f"{i+1}° APOSTA: {sorted(l)}")







