""" masc = 'M'
fem = 'F'
sexo = 'a'
while sexo == masc or fem:
    print('-=-' * 20)
    print("BEM VINDO AO SISTEMA DE LEITURA DE SEXOS")
    print('-=-'*20)
    print(" ")
    print('Digite se você for homem  [M]')
    print('Digite se você for mulher [F]')
    sexo = str(input('DIGITE SEU SEXO >>')).upper()
    if sexo == 'F':
        print('Você é ela')
    elif sexo == 'M':
        print('Você é ele')
    else:
        print("ERROR!!!")"""

masc = 'M'
fem = 'F'
sexo = 'a'
while sexo != masc and sexo != fem:
    print("DIGITE SE VOCÊ FOR MULHER [F]")
    print("DIGITE SE VOCÊ FOR HOMEM  [M]")
    sexo = str(input("Digite seu sexo >>")).upper()
    if sexo == 'M':
        print("Você é macho")
    elif sexo == 'F':
        print("Você é femea")
    else:
        print("ERROR!!! DIGITE NOVAMENTE")
        print('-=-'*25)
        print(" ")
