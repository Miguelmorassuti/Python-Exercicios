#utilizando variáveis dentro do laço
for p in range(1,6):
    peso = int(input(f"DIGITE O SEU PESO {p}º>> "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior = peso
        if peso <menor:
            menor = peso
print(f"O maior peso foi de {maior} e o menor foi de {menor}")
