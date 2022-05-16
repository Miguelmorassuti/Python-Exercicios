acertos=0
print("SUPER JOGO ULTRA LEGAL DE PAR OU IMPAR")
import random
Lista = ["PAR" , "IMPAR"]
while True:
    escolhido = random.choice(Lista)
    esc= str(input("PAR OU IMPAR? >>")).upper()
    if esc == escolhido:
        print("Acertou, continue jogando")
        acertos+=1
    else:
        print("ERROUUUUUUU :(")
        break
print(f"Ao todo o jogador teve {acertos} acertos consecutivos")

