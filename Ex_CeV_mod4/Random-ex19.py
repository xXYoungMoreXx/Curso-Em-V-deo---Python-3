from random import choice
a1 = str(input('Nome do 1° Aluno: '))
a2 = str(input('Nome do 2° Aluno: '))
a3 = str(input('Nome do 3° Aluno: '))
a4 = str(input('Nome do 4° Aluno: '))
lista = [a1, a2, a3, a4]
aluno = (choice(lista))
print('O aluno escolhido foi: {}'.format(aluno))
