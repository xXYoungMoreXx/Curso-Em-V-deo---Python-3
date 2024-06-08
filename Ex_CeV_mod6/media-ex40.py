a1 = str(input('Digita o nome d@ alun@: '))
u1 = float(input('Digite a nota d@ alun@ na 1° unidade: '))
u2 = float(input('Digite a nota d@ alun@ na 2° unidade: '))
u3 = float(input('Digite a nota d@ alun@ na 3° unidade: '))
print('-=-'*10)
me = u1 + u2 + u3 / 3
# presumindo que a note minima seja 5
print('O Aluno tirou nota {} na 1°, {} na 2° e {} na 3°.'.format(u1, u2, u3))
print('Finalizando o ano letivo com média {:.1f}.'.format(me))
print('-=-'*10)
if me == 5:
    print('Alun@ aprovad@ com note {:.1f}. Precisa melhorar!'.format(me))
elif me > 5:
    print('Alun@ Aprovad@ com nota {:.1f}. Excelente!'.format(me))
else:
    print('Alun@ reprovad@ com nota {:.1f}.'.format(me))
    print('Tente novamente no próximo ano.')
