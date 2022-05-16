import random
pri = str(input("Nome do primeiro aluno >>"))
seg = str(input("Nome do segundo aluno >>"))
ter = str(input("Nome do terceiro aluno >>"))
qua = str(input("Nome do quarto aluno >>"))
lista = [pri, seg, ter, qua]
esc = random.choice(lista)
print(f"O escolhido foi: {esc} ")
