seg1 = input('Primeiro segmento: ')
seg2 = input('Segundo seguimento: ')
seg3 = input('Terceiro seguimento: ')
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os seguimentos formam um triângulo', end=' ')
    if seg1 == seg2 == seg3:
        print('equilátero!')
    elif seg1 != seg2 != seg3 != seg1:
        print('escaleno!')
    else:
        print('isóceles!')
else:
    print('Os seguimentos não podem formar um triangulo.')
