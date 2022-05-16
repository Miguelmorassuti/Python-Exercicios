from datetime import date
ano = date.today().year
nasc = int(input("Digite o ano de seu nascimento >>"))
idade = ano-nasc
if idade<=9:
    print("CATEGORIA MIRIM")
elif 9<idade<=14:
    print("CATEGORIA INFANTIL")
elif 14<idade<=19:
    print("CATEGORIA JUNIOR")
elif 19<idade<=25:
    print("CATEGORIA SÊNIOR")
elif idade>25:
    print("CATEGORIA MASTER")