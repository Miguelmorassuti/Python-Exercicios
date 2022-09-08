#Nícolas Lelis de Oliveira - RA: 617032
#Miguel Guimarães Morassuti - RA: 621927
    
tabela = [
          [0, 0, 1, 0],
          [0, 2, 1, 0],
          [3, 0, 1, 0],
          [0, 0, 1, 1]               #1 da coluna da direita indica que essa é coluna do estado final
          ]

dicio = {
         "a":0,
         "b":1,
         "c":2
         }

linha = cont = 0

palavra = input("Digite a palvra: ")


for i in palavra:                   #percore cada letra da variavel palavra
    if i not in dicio.keys():
        cont=+1
        continue                    #codigo se encerra se houver um digito != A, B, C

    elif cont>0:
        break

    else:
        linha = tabela[linha][dicio[i]]


if tabela[linha][3] == 1 and cont==0:     #se ao terminar a execução do codigo a coluna final for igual 1 a palavra é valida
    print("Palavra válida!")
else:
    print("Palavra inválida!") 










