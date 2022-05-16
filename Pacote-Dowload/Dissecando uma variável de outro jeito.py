algo = input('Digite algo:')
print(f'Qual o tipo primitivo do item digitado? {type(algo)}')
print(f'É composto de valores imprimiveis? {algo.isprintable()}')
print(f'É composto por letras ou números? {algo.isalnum()}')
print(f'É composto apenas por letras? {algo.isalpha()}')
print(f'É composto apenas por decimais? {algo.isdecimal()}')
print(f'É composto apenas por digitos? {algo.isdigit()}')
print(f'É um identificador de codigo? {algo.isidentifier()}')
print(f'É composto apenas por letras minusculas? {algo.islower()}')
print(f'É composto apenas por números? {algo.isnumeric()}')
print(f'É composto apenas por espaços? {algo.isspace()}')
print(f'É um valor capitalizado? {algo.istitle()}')
print(f'É composto apenas por letras maiusculas? {algo.isupper()}')




