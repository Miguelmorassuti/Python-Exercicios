#FUNÇÃO SEM PARAMETROS
def mostralinha():
    print('-=-'*5)
mostralinha()
print("miguel")
mostralinha()



"""""#FUNÇÃO COM PARAMETROS
def texto(abc):
    mostralinha()
    print(abc)
    mostralinha()
texto('sistema de sla')"""



"""""#FUNÇÃO COM NÚMEROS E PARAMETRO (SO FUNCIONA COM A MESMA QUANTIDADE DE PARAMETROS E NUMEROS)
def soma(a,b):
    print(f"A SOMA DE {a} + {b} RESULTA EM ==> {a+b}")
soma(5,6)       #se não declarar o valor de A e B o pc entende que o primeiro q aparece é o A e o segundo é o B
soma(2,1)       #porem esse codigo so funciona com 2 numeros devido apenas ter 2 parametros declarados"""



"""#FUNCÃO COM NÚMEROS E PARAMTEROS(ATRAVÉS DE CONTADOR, FUNCIONA COM QUALQUER QUANTIDADE DE NÚMEROS
def cont(* núm):  #UTILIZANDO *num É POSSÍVEL MEXER COM QUALQUER QUANTIDADE DE NÚMEROS
    for p in núm:
        print(p, end=" ")
    print("END")
cont(3,2,1)
cont(8)
cont(1,4)"""


#USANDO LEN
def teste(*num):
    quantidade = len(num)
    print(f"RECEBI OS VALORES {num} e são ao todo {quantidade}")
teste(3,1,2)
teste(3,6)
teste(1)


#EXEMPLO, DOBRANDO ITENS DE UMA LISTA
def dobra(lst):
    cont = 0
    while len(lst) > cont:
        lst[cont]*= 2
        cont += 1


numeros = [3,2,10,5]
dobra(numeros)
print(numeros)




