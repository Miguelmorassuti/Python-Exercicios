print("-=-=-=MENU DE CÁLCULOS=-=-=-")
n1= float(input("DIGITE O PRIMEIRO NÚMERO >>"))
n2= float(input("DIGITE O SEGUNDO NÚMERO >>"))
resp = 999
while resp != 6:
    print("-=-"*20)
    print("""O QUE DESEJA FAZER?
    SOMAR NÚMEROS----------[1]
    SUBTRAIR NÚMEROS-------[2]
    MULTIPLICAR OS NÚMEROS-[3]
    DIVIDIR OS NÚMEROS-----[4]
    DIGITAR NOVOS NÚMEROS--[5]
    SAIR DO MENU-----------[6]""")
    resp = int(input("SUA RESPOSTA --> "))
    if resp == 1:
        print(f"A soma entre {n1} + {n2} resulta em --> {n1+n2}")
    elif resp ==2:
        print(f"A subtração entre {n1} - {n2} resulta em --> {n1-n2}")
    elif resp ==3:
        print(f"A multiplicação entre {n1} X {n2} resulta em --> {n1 * n2}")
    elif resp == 4:
        print(f"A divisão entre {n1} / {n2} resulta em --> {n1 / n2}")
    elif resp == 5:
        n1 = float(input("DIGITE O PRIMEIRO NÚMERO >>"))
        n2 = float(input("DIGITE O SEGUNDO NÚMERO >>"))
    else:
        print("ERROR!! DIGITE NOVAMENTE")
print("FOI UM PRAZER TRABALHAR COM VOCÊ!!")
