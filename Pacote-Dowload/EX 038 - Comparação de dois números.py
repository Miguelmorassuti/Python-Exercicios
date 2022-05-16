print("HI FRIEND, I WILL COMPARE THREE NUMBERS")
n1 = int(input("DIGITE O PRIMEIRO NÚMERO:"))
n2 = int(input("DIGITE O SEGUNDO NÚMERO:"))
n3 = int(input("DIGITE O TERCEIRO NÚMERO:"))
if n1>n2>n3:
    print(f"O valor {n1} é maior que {n2} e ambos os valores são maiores que {n3}")
elif n1>n3>n2:
    print(f"O valor {n1} é maior que {n3} e ambos os valores são maiores que {n2}")
elif n2>n1>n3:
    print(f"O valor {n2} é maior que {n1} e ambos os valores são maiores que {n3}")
elif n2>n3>n1:
    print(f"O valor {n2} é maior que {n3} e ambos os valores são maiores que {n1}")
elif n3>n2>n1:
    print(f"O valor {n3} é maior que {n2} e ambos os valores são maiores que {n1}")
elif n3>n1>n2:
    print(f"O valor {n3} é maior que {n1} e ambos os valores são maiores que {n2}")
elif n1==n2==n3:
    print("TODOS SÃO IGUAIS")

