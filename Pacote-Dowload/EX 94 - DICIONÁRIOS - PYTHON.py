# Um programa que lê nome e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. no final, mostra:
# A) Quantas pessoas cadastradas
# B) A média de idade
# C) Uma lista com mulheres
# D) Uma lista com idade acima da média.

armazenamento = {}
dados = []
soma = 0
mulheres = []

while True:
    armazenamento.clear()     #CLEAR PARA APAGAR OS DADOS DA PESSOA ANTERIOR (JA INSERIDA NO DICIONÁRIO)

    armazenamento['NOME'] = str(input("NOME ==>")).upper().strip()
    armazenamento['SEXO'] = str(input("SEXO [M/F] ==>")).upper().strip()
    while armazenamento['SEXO'][0] not in "MF":
        print("OPÇÃO INEXISTENTE, TENTE NOVAMENTE")
        armazenamento['SEXO'] = str(input("SEXO [M/F] ==>")).upper().strip()
    armazenamento['IDADE'] = int(input("IDADE ==>"))
    soma +=armazenamento['IDADE']

    dados.append(armazenamento.copy())  #INSERINDO DADOS DO DICIONÁRIO NA LISTA, PARA ISSO É NECESSÁRIO O .COPY

    esc = str(input("DESEJA CONTINUAR? [S/N] ==>")).upper().strip()
    while esc[0] not in "SN":
        print("OPÇÃO INEXISTENTE, TENTE NOVAMENTE")
        esc = str(input("DESEJA CONTINUAR? [S/N] ==>")).upper()
    if esc == "N":
        break

#ANALISANDO DADOS

print("=-="*18)
# A) Quantas pessoas cadastradas
print(f"AO TODO FORAM REGISTRADAS {len(dados)} PESSOAS ")

print("=-="*18)

# B) A média de idade
print((f"A MÉDIA DE IDADE É DE {soma/len(dados):.1f} ANOS"))
print("=-="*18)

# C) Uma lista com mulheres
print(f"AS MULHERES NA LISTA SÃO:", end=" ")
for c in dados:
    if c['SEXO'] in 'F':
        print(f' {c["NOME"]}', end=" ")

print("\n-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")

# D) Uma lista com idade acima da média.
media = soma/len(dados)
print(f"OS QUE ESTÃO COM IDADE ACIMA DA MÉDIA SÃO:", end=" ")
for m in dados:
    if m['IDADE'] > media:
        print(f' {m["NOME"]}', end=' ')

