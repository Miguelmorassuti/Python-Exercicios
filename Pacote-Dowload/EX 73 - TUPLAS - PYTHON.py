print("-=-"*18)
print("BRASILEIRÃO 2021")
print("-=-"*18)
timesordem = "GALO" , "FLAMENGO" , "PALMEIRAS" , "FORTALEZA" , "CORINTHIANS" , "BRAGANTINO" , "FLUMINENSE" , \
               "AMERICA" , "ATLETICO GOIANIENSE" , "SANTOS" , "CEARÁ" , 'INTER' , "SPFC" , "ATLETICO-PR " ,\
             "CUIABA" , "JUVENTUDE" , "GREMIO" , "BAHIA" , "SPORT" , "CHAPE"
print("O que deseja saber:")
print("[1] Os 5 primeiros")
print("[2] Os 4 rebaixados")
print("[3] Os times que participaram do campeonato em ordem")
print("[4] Posição em que o SPFC ficou no campeonato")
print("")
esc = 0
#esc = int(input("DIGITE SUA ESCOLHA ->"))
while esc != 1 or 2 or 3 or 3 or 4:
    esc = int(input("DIGITE SUA ESCOLHA ->"))
    if esc == 1:
        print(("Os 5 primeiros ->"), timesordem[0:5])
        break
    elif esc ==2:
        print(("Os 4 rebaixados ->"), timesordem[16:20]) #-4:  tambem da certo
        break
    elif esc ==3:
        print(("Os times que participaram do campeonato em ordem ->") , sorted(timesordem))
        break
    elif esc ==4:
        print(("O time do SPFC acabou o campeonato na posição n° ->") , (timesordem.index("SPFC")+1))
        break
    else:
        print("OPÇÃO INVALIDA!!! \
    ESCOLHA NOVAMENTE!!!")
        print("-=-"*16)

