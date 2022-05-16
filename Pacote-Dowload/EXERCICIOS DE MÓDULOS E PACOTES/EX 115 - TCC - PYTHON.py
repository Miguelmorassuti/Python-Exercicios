def MOSTRALINHA():
    print("-=-"*20)



def MENUCADASTRO():

    #MENU PARTE VISUAL

    MOSTRALINHA()
    print("\033[3;31mMENU PRUNCIPAL\033[m")
    MOSTRALINHA()
    print("\033[3;31m1 -\033[m \033[1;32mPESSOAS CADASTRADAS")
    print("\033[3;31m2 -\033[m \033[1;32mNOVO CADASTRO")
    print("\033[3;31m3 -\033[m \033[1;32mSAIR DO SISTEMA\033[m")
    MOSTRALINHA()

    #AQUI A MAGIA ACONTECE

def ENGENHARIACADATRO():
    CADASTRADOS = {}
    while True:
        try:
            esc = int(input("\033[3;31mDIGITE SUA ESCOLHA -->\033[m"))
        except ValueError:
            MOSTRALINHA()
            print("\033[3;33mERRO!!!, ESCOLHA UMA OPÇÃO ENTRE 1,2 OU 3\033[m")
            MENUCADASTRO()
            continue
            return 0
        else:                               #SE TUDO TIVER OK, EXECUTE O CODIGO DAQUI PRA BAIXO
            if esc == 2:
                CADASTRADOS["NOME"] = input("NOME -->")
                CADASTRADOS["IDADE"] = input("IDADE -->")
                while not CADASTRADOS["IDADE"].isnumeric():
                    del CADASTRADOS["IDADE"]
                    CADASTRADOS["IDADE"] = input("IDADE")
                    print("DADOS CADASTRADOS COM SUCESSO")

            if esc == 3:
                cont=0
                definitiva = CADASTRADOS.copy()
                for c, v in definitiva.items():
                    if cont %2 ==0:
                        print(f"O {cont+1}° CADASTRADO SE CHAMA {v} ")
                    else:
                        print(f"POSSUI {v} ANOS")
                    cont +=1
                break







MENUCADASTRO()
ENGENHARIACADATRO()