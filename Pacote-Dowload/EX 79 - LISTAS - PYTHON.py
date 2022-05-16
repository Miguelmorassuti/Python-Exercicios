valores = []
while True:
    valor = int(input("Digite um valor -->"))
    if valor in valores:
        print("VALOR DUPLICADO, TENTE OUTRO ...")
    else:
        print("VALOR ADICIONADO COM SUCESSO ...")
        valores.append(valor)

    esc = str(input("DESEJA CONTINUAR? \
            \nSe sim digite [S] \
            \nSe não digite [N] \
            \nSUA RESPOSTA -->")).upper().strip()[0]
    if esc[0] not in  "sSNn":
        print("-=-" * 18)
        print("OPÇÃO INVALIDA")
        print("VOLTE AO INICIO ...")
        print("-=-"*18)
    elif esc == "S":
        print("-=-"*18)
    elif esc == "N":
        valores.sort()
        print(f"Lista formada --> {valores}")
        break


