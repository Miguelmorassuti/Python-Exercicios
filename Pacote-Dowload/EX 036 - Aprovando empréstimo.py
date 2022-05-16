#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

nome = str(input("Digite seu nome por favor >>"))
print(f"BEM VINDO ao sistema automatico de validação de financiamento {nome} ")
v1 = float(input("Qual o valor do imovel desejado? R$"))
s = float(input("Qual é a sua renda media mensal? R$"))
t = int(input("Em quantos anos você quer financiar o imôvel? >>"))
meses = t*12
fina = v1/meses
if fina<(s/100)*30:
    print("Seu financiamento foi aprovado")
else:
    print(f"Para financiar esse imóvel o valor minimo mensal é de R${fina:.2f}")
    print("FINANCIAMENTO NEGADO")