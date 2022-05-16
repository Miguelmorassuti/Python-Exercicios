n1 = float(input("Digite um número >>"))
n2 = float(input("Agora outro número >>"))
n3 = float(input("Mais um por favor, juro que é o ultimo kkkk>"))
#verificando o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print((f"O menor número digitado foi o "), menor)
#verificando o maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print((f"O maior número digitado foi o "), maior)

