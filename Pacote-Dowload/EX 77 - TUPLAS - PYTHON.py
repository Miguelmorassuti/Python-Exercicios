palavras = "AMOR" , 'SOLIDARIEDADE' , 'ALEGRIA' , 'FELICIDADE' , 'TRISTEZA' , 'SABEDORIA' , 'PACIENCIA', \
    'ESPIRITO' , 'PAIXAO' , 'INTELIGENCIA'
for un in palavras:
    print(f"\nNa palavra {un} temos com vogais as letras -->", end=' ')
    for letra in un:
      if letra.lower() in "aeiou":
        print(letra, end=' ')