frase = str(input("Digite algo e direi se é um palíndromo :")).upper().strip()
palavras =frase.split()
junto = ''.join(palavras)
inverso = " "
for abc in range (len(junto) -1, -1, -1 ):
    inverso += junto[abc]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print(f" A frase {frase} é um palíndromo de {abc}")
else:
    print(f"A frase {frase} NÃO é um palíndromo de {abc}")




