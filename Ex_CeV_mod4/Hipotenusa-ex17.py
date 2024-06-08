from math import hypot, trunc
co = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co, ad)
print('O comprimento da hipotenusa é : {}'.format(trunc(hip)))
