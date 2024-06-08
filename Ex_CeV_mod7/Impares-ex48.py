Acum = 0
Cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        Acum += n
        Cont += 1
print('''Há {} números impares, multiplos de 3, de 0 a 500.
A soma deles é igual a: {}'''.format(Cont, Acum))
