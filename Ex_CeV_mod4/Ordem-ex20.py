from random import shuffle
a1 = input('Digite o nome do 1° Aluno: ')
a2 = input('Digite o nome do 1° Aluno: ')
a3 = input('Digite o nome do 1° Aluno: ')
a4 = input('Digite o nome do 4° Aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem da sala, será: {}'.format(lista))
