num = esc = cont = 0
while num != 999:
    num = int(input("Digite algum número, ou tecle [999] para parar >>"))
    esc +=1
    if num !=999:
        cont += num
print(f"Ao todo foram digitados {esc - 1} números, sendo que a soma deles resulta em: {cont}")


