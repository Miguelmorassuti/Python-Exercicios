somaid = 0
masc = 0
fem = 0
somapeso = 0
mulhermenor = 0
for p in range (1,5):
    print(f" -=--=--=-==-=-={p}º PESSOA -=-=--=-=-=-=-=-")
    nome = input("NOME:")
    idade = int(input("IDADE:"))
    somaid += idade
    peso = float(input("PESO:"))
    genero = str(input(" \n [F] se feminino \n [M] se masculino \n informe seu gênero:")).upper().strip()

    if genero == 'M':
        masc = masc + 1
    else:
        fem = fem + 1
    if p ==1:
        somapeso = peso
    if somapeso < peso:
        somapeso = peso
        name = nome
    if genero in "fF" and idade<20:
        mulhermenor =+1
print(f"A média de idade desse grupo é de {(somaid/4):.2f} anos")
print(f"Nesse grupo tem {masc} homens e {fem} mulheres")
print(f"Ao todo {mulhermenor} mulheres tem menos do que 20 anos")
print(f"O maior peso obtido foi o de {name}, possuindo {somapeso}KG ")




