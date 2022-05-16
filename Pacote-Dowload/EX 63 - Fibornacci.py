qtd = int(input('Digite a quantidade de termos de fibonnaci que deseja saber: '))
anterior = 0
posterior = 0
c = 0

while c < qtd:
    print(posterior)
    posterior += anterior
    anterior = posterior - anterior
    if posterior ==0:
        posterior += 1
    c += 1