print("-=-"*18)
print(f'{"LISTAGEM DE PREÇOS":^52}') #tecnica para centralizar texto
print("-=-"*18)
print("--"*26)
tupla = "lapis" , 1.75 , "borracha" , 2.00 , 'caderno' , 15.90 , 'estojo' , 25.00 , 'trasnferidos' , 4.20 , \
        'compasso' ,  9.99 , 'mochila' , 120.32 , 'canetas' , 22.32, 'livro' , 34.90
for un in range(0,len(tupla),2):
    print(f"{tupla[un]:.<40}", f" R$ {tupla[un + 1]:>7.2f}")



