# Faça um programa que leia um número inteiro e diga se ele é um número primo
n1 = int(input('Digite um número: \033[32m'))
cont = 0
print('\033[mNa sequência: ',  end="")
for c in range(1, n1+1):
    if n1 % c == 0:
        cont += 1
        print('\033[33m', end="")
    else:
        print('\033[31m', end="")
    print('{}'.format(c), end=" ")
if cont == 2:
    print("\n\033[32m{}\033[m é primo!".format(n1))
else:
    print('''\n\033[32m{}\033[m não é primo por ser divísivel por \033[32m{}
\033[mnúmeros.'''.format(n1, cont))
