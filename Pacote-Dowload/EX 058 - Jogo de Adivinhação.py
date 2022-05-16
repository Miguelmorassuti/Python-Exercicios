import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
adiv = random.choice(lista)
resp = 'a'
tentativas = 0
print("HELLO, I AM YOUR MACHINE, PLAY WITH ME")
print("-=-"*20)
while resp != adiv:
    resp = int(input("DIGITE SEU PALPITE [0 a 10] >>"))
    tentativas += 1
    if resp > adiv:
        print("UM POUCO MENOS...")
    elif resp<adiv:
        print("UM POUCO MAIS...")
    print("-=-"*20)
print(f"UOUUUUU, VERY GOOD, ITS THE NUMBER {adiv}")
print(f"AO TODO VOCÊ PRECISOU DE {tentativas} TENTATIVAS PARA ACERTAR")

