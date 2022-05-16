#impor random é para sortear
#from time import sleep é um temporizador (deixa o efeito "processando")

from time import sleep
import random
print("-=-=-="*15)

print("VOU ADIVINHAR UM Nº DE 0 A 5, TENTE ADIVINHAR..")
adiv = int(input("Digite o nº que você acha que eu adivinhei >> "))
lista = [0,1,2,3,4,5]
print("PROCESSANDO....")
sleep(2)
esc = random.choice(lista)
if adiv==esc:
    print("PARÁBENS, VOCÊ ACERTOU MINHA ADIVINHAÇÃO")

else:
    print((f"VOCÊ ERROU, O NUMERO QUE EU PENSEI FOI O>>"),esc )

print("__________________________fim_______________________________")