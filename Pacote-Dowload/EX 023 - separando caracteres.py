n=int(input("Olá, digite um número:"))

#se fizer sem esse esquema abaixo de conversão, não funciona quando tem menos de 4 caracteres

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000% 10
print((f"Analisando o número:") , (n))
print((f'Unidade:') , (u))
print((f'Dezena:') , (d))
print((f'Centena:') , (c))
print((f'Milhar:') , (m))


