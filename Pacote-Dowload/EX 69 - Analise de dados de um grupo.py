print("-=-"*18)
print("CADASTRE UMA PESSOA")
print("-=-"*18)
maiores = homens = novinhas = 0
while True:
    sexo = str(input("DIGITE O SEXO [F/M]  >>")).upper().strip()[0]
    while sexo not in 'MF':
        print("ERROR! DIGITE NOVAMENTE")
        sexo = str(input("DIGITE O SEXO [F/M]  >>")).upper().strip()[0]
    idade = int(input("DIGITE A IDADE >>"))
    if idade > 18:
        maiores +=1
    if sexo=='M':
        homens +=1
    if sexo=="F" and idade<20:
        novinhas +=1
    print("-=-" * 18)
    continuar = str(input("DESEJA CONTINUAR? [S/N] >")).upper().strip()
    if continuar == 'N':
        break
    print("-=-" * 18)
print(f"Ao todo {maiores} pessoas são maiores de idade, {homens} são homens e {novinhas} são mulheres abaixo dos 20  anos")
