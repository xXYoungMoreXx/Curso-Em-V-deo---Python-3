n1 = int(input('Digite um número de 0 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('='*35)
print('Este número tem {} unidades'.format(u))
print('Este número tem {} dezenas'.format(d))
print('Este número tem {} centenas'.format(c))
print('Este número tem {} milhares'.format(m))
