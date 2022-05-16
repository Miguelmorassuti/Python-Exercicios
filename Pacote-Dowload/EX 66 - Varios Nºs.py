cont = somatoria = 0
while True:
    print("-=-"*20)
    num = int(input("""DIGITE ALGUM NÚMERO
Caso queira parar digite [ 999 ]
Número escolhido >>"""))
    if num == 999:
        break
    cont += 1
    somatoria += num
print(f"Ao todo foram digitados {cont} Nºs, sendo que a somatoria entre eles resulta em {somatoria}")