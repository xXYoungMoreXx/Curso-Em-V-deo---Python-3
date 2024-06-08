from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('-=-'*12)
print('Aguarde...')
sleep(3)
print('-=-'*12)
if n1 > n2:
    print('{} é maior que {}!'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}!'.format(n2, n1))
else:
    print('Os dois números são iguais!')
