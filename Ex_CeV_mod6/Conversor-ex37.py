import time
print('-=-'*12)
n1 = int(input('Digite um número: '))
print('-=-'*12)
print('''[ 1 ] = Binário
[ 2 ] = Hexadécimal
[ 3 ] = Octal''')
print('-=-'*12)
c1 = int(input('escolha uma opção: '))
print('-=-'*12)
print('Aguarde...')
time.sleep(2)
print('-=-'*12)
if c1 == 1:
    print('"{}" Em bínário é: {}'.format(n1, bin(n1)[2:]))
elif c1 == 2:
    print('"{}" Em hexadécimal é: {}'.format(n1, hex(n1)[2:]))
elif c1 == 3:
    print('"{}" Em octal é: {}'.format(n1, oct(n1)[2:]))
else:
    print('Opção inválida! tente novamente.')
print('-=-'*12)
