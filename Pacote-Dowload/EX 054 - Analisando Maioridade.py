from datetime import date
atual = date.today().year
a = 1
somatoria = 0
for a in range (1 ,8, ++a):
    ano = int(input(f"Digite o ano em que você nasceu {a}º>>"))
    idade = atual - ano
    if idade > 17:
        somatoria += 1
print(f" Nesse grupo de pessoas {somatoria} são maiores de idade e {7 - somatoria} não são")



