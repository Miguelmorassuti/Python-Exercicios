def LeiaDin(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == " ":
            print("\033[3,31mERRO!!!\033[m")
        else:
            valido = True
            return float(entrada)