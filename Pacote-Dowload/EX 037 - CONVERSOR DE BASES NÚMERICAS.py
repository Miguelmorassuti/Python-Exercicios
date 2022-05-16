
print("EU SOU UM SUPER PROGRAMA DE CONVERSÃO PROGRAMADO PELO MESTRE MIGUEL ")
num1 = int(input("Digite um número para mim converter para outro sistema de numeração:"))
print("Para converter em binário digite       [1]")
print("Para converter para octal digite       [2]")
print("Para converter para hexadecimal digite [3]")
decisao = int(input("Para qual base númerica você quer que eu traduza?"))
if decisao == 1:
    print("O número decimal", num1, "em binário possui o valor de", bin(num1)[2:])
elif decisao == 2:
    print("O número decimal", num1, "em octal possui valor de", oct(num1)[2:])
elif decisao==3:
    print("O número decimal", num1, "em hexadecimal possui valor de", hex(num1)[2:])
else:
    print("OPÇÃO INVÁLIDA")


