"""lista = []
lista.append("MIGUEL")
lista.append(18)
men = lista[:] #se n colocar colchetes e 2 pontos tudo o que acontecer em uma variavel acontece na outra
lista.append("AMABILLY")
lista.append(11)
print(lista)
print(men)"""

familiares = [["Paulo",41] , ["Zenaide",45], ["AMABILLY", 11], ["MIGUEL", 18]]
print(*familiares[1], sep= ' ')        #vai aparecer -->   zenaide 45
print(familiares[1][1])                #vai aparecer -->   45
print(familiares[3][0])                #vai aparecer -->   MIGUEL
print(familiares[3])                   #vai aparecer --> ['MIGUEL', 18]
print(" ")

## USANDO LAÇOS

#for i in familiares:
#    print(i)                           #vai aparecer cada nome e cada idade em linha por linha
#    print(i[0])                        #vai aparecer apenas o nome de todos
#    print(i[1])                        #vai aparecer apenas as idades

# USANDO FOR IN RANGE
dado = []
for a in range (0,3):
    dado.append(str(input("DIGITE SEU CARRO: ")))
    dado.append(str(input("DIGITE O ANO DO CARRO: ")))
dados = dado[:]
dado.clear()                            #clear serve para apagar a variavel dado, ela não se faz necessaria
print(dados)               #devido que a variavel dados recebeu todos os dados que estavam armazenados nela

