#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.

print("\033[7;31;40m~~"*18)
print("\033[7;30;41mSISTEMA DE AJUDA MYHELP")
print("\033[7;31;40m~~"*18)

def MYHELP():
    while True:
        esc = input("\033[4;30;41mBIBLIOTECA OU FUNÇÃO:")
        help(esc)

        cont = str(input("DESEJA CONTINUAR? [S/N] ==>")).strip().upper()
        if cont[0] == "N":
            break
        elif cont[0] not in "SN":
            while cont[0] not in "SN":
                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!")
                cont = str(input("DESEJA CONTINUAR? [S/N] ==>")).strip().upper()
                if cont[0] == "N":
                    break
            break

MYHELP()