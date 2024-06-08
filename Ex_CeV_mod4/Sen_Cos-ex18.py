from math import sin, cos, tan, radians
ang = (float(input('Digite um ângulo: ')))
print('='*45)
print('O ângulo de {}° tem a seno: {:.2f}°'.format(ang, sin(radians(ang))))
print('O ângulo de {}° tem a Cosseno: {:.2f}°'.format(ang, cos(radians(ang))))
print('O ângulo de {}° tem a Tangente: {:.2f}°'.format(ang, tan(radians(ang))))
print('='*45)
