#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com
#valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
print("\033[3;33;40m MATRIZ 3X3\033[m")
matriz = [[], [], [], [], [], [], [], [], []]
for x in range(0,9):
    matriz[x].append(int(input(f'DIGITE O VALOR PARA A POSIÇÃO {x}: ')))
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])