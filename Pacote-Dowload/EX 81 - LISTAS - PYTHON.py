#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:  A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

l= []
while True:
    l.append(int(input("DIGITE UM NÚMERO -->")))
    esc = (str(input("DESEJA CONTINUAR [S]/[N]? -->")).upper().strip())
    if esc[0] =="N":
        print("-=-"*18)
        print((f"AO TODO FORAM DIGITADOS {len(l)} NÚMEROS"))
        l.sort(reverse=True)
        print(f"A LISTA FORMADA EM ORDEM DECRESCNTE --> ", end=' ')
        print(*l, sep=', ')

        if 5 in l:
            print("O VALOR 5 ESTA NA LISTA")
        else:
            print("O VALOR 5 NÃO ESTA NA LISTA")
        break
    elif esc[0] =="S":
        print("-=-"*18)
    else:
        while esc[0] not in ("SN"):
            print("OPÇÃO INVALIDA!!!")
            esc = (str(input("DESEJA CONTINUAR [S]/[N]? -->")).upper().strip())
        if esc[0] == "N":
            print("-=-" * 18)
            print((f"AO TODO FORAM DIGITADOS {len(l)} NÚMEROS"))
            l.sort(reverse=True)
            print(f"A LISTA FORMADA EM ORDEM DECRESCNTE --> ", end=' ')
            print(*l, sep=', ')

            if 5 in l:
                print("O VALOR 5 ESTA NA LISTA")
            else:
                print("O VALOR 5 NÃO ESTA NA LISTA")
            break
