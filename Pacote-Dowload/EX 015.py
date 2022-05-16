print("Olá, bem vindo ao nosso sistema de pagamentos, vamos calcular sua dívida!")
d=int(input("Quantos dias você ficou com a posse do carro? :"))
km=float(input('Quantos KMs foram rodados com o carro? :'))
print(f' Você deverá pagar em diarias pelo carro o valor de: R${d*60} e R${km*0.15} pelos KMs rodados, totalizando num pagamento de {(d*60)+(km*0.15)}')
