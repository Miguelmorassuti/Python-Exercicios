nome = str(input("Digite o seu nome:")).strip()
print(nome.upper())
print(nome.lower())
#len conta as letras e com a junção da função count a maquina nao conta os espaços
print(("Seu nome tem:") , (len(nome)) - (nome.count(" ")) , ("letras"))
#contando so as primeiras letras do nome
print(("Seu primeiro nome tem:") , (nome.find(" ")) , ("letras"))
