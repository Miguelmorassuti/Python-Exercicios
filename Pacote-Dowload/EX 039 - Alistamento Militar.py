print("TIRO DE GUERRA 57º")
idade = int(input("Digite sua idade jovem >>"))
if idade<18:
    print("AINDA NÃO CHEGOU O MOMENTO DE VOCÊ SERVIR A NAÇÃO")
    print(f"FALTA(M) {18-idade} ANO(S) PARA VOCÊ SERVIR SEU PAÍS")
elif idade==18:
    print(f"CHEGOU O MOMENTO, VOCÊ ESTA CONVOCADO, BEM VINDO AO BATALHÃO RECRUTA!!")
elif idade>18:
    print(f"SEU ALISTAMENTO ESTA ATRASADO EM {idade-18} ANO(S), VOCÊ ESTA CONVOCADO SEU FUJÃO!!")

    