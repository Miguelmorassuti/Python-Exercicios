f = float(input('Digite a temperatura em Fahrenheit que voce quer converter-->'))
c = ((f-32)/9)*5
k = c+273
print("ESCOLHA A BASE DE TEMPERATURA PARA CONVERSÃO")
print("[1] CELSIUS")
print("[2] KELVIN")
esc = int(input("SUA ESCOLHA-->"))
if esc == 1:
    print(f" A temperatura {f} convertida para CELSIUS representa a temperatura {c:.1f}º")
elif esc == 2:
    print(f" A temperatura {f} convertida para KELVIN representa a temperatura {k:.1f}º")
elif esc != 1 or 2:
    print("COMANDO INVALIDO!!!")