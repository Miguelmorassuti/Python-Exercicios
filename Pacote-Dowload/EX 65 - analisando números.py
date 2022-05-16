somatoria = 0
quant= 0
maior = 0
menor = 99999
cont = True
while cont == True:
    num= int(input("Digite algum número >>"))
    quant +=1
    somatoria += num
    if num>maior:
        maior = num
    elif num<menor:
        menor = num
    esc= str(input("Deseja continuar [S/N] >>")).upper()
    if esc == "N":
        cont = False
    elif esc == "S":
        print("-=-"*15)
    else:
        print("ERROR! DIGITE NOVAMENTE")
media = somatoria/quant
print("-=-"*20)
print(f"Ao todo foram digitados {quant} Nºs, sendo o maior o Nº {maior} e o menor o Nº {menor}, \n a media entre os valores é de {media}")

