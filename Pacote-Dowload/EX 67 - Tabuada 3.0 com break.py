print("-=-=-=-TABUADA 3.0-=-=-=-")
while True:
    num = int(input("Digite qual tabuada deseja saber (se deseja sair tecle algum nº negativo) >>"))
    if num < 0:
        break
    for tabu in range (1,11):
        print(f"{num} X {tabu} = {num*tabu}")