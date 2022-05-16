l1 = int(input("QUAL O TAMANHO DO 1º LADO DO TRIÂNGULO>>"))
l2 = int(input("QUAL O TAMANHO DO 2º LADO DO TRIÂNGULO>>"))
l3 = int(input("QUAL O TAMANHO DO 3º LADO DO TRIÂNGULO>>"))
if l1+l2>=l3 and l1+l3>=l2 and l2+l3>=l1:
    print("ESSES LADOS PODEM FORMAR UM TRIÂNGULO!!!")
    if l1==l2==l3:
        print("O TRIâNGULO FORMADO É EQUILÁTERO")
    elif l1==l2!=l3 or l2==l3!=l1 or l1==l3!=l2:
        print("O TRIANGULO FORMADO É ISOCELES")
    else:
        print("O TRIÂNGULO FORMADO É ESCALENO")
else:
    print("ESSES LADOS NÃO PODEM FORMAR UM TRIÂNGULO")



