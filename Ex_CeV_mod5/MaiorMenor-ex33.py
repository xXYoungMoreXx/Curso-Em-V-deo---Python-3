n1 = int(input('Qual será o primeiro número? '))
n2 = int(input('Qual será o segundo número? '))
n3 = int(input('Qual será o terceiro número? '))
print('-=-'*10)
menor = n1
if n1 < n2 and n1 < n3:
    print('{} É o menor número'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} É o menor número'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} É o menor número.'.format(n3))
if n1 > n2 and n1 > n3:
    print('{} É o maior número.'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} É o maior número.'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} É o maior número.'.format(n3))
