print("Bem vindo ao Mundo 3 do curso do python")
print("-=-"*20)
num = "Zero" , "UM" , "DOIS" , "TRES" , "QUATRO" , "CINCO" , "SEIS" , "SETE" , "OITO" , "NOVE" ,\
      "DEZ" , "ONZE" , "DOZE" , "TREZE" , "QUATORZE" , "QUINZE" , "DEZESSEIS" , "DEZESSETE"  ,\
      "DEZOITO" , "DEZENOVE" , "VINTE"
esc = 21
while esc > 20:
    esc = int(input("Digite em algarismo algum n° que direi seu nome >>"))
    if esc < 21 > -1:
        break
    else:
        print("OPS! Nº INVALIDO TENTE NOVAMENTE!!!")
        print("-=-" *20)
print(("VOCÊ DIGITOU O Nº" ) , num[esc])
