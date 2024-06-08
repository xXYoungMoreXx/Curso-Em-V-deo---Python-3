import random
from time import sleep
pc = random.randint(1, 3)
print('='*10, 'JOKENPO!', '='*10)
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
print('=-='*10)
jogador = int(input('Qual a sua jogada? '))
print('=-='*10)
if jogador == 1:
    print('Você jogou: PEDRA')
elif jogador == 2:
    print('Você jogou: PAPEL')
elif jogador == 3:
    print('Você jogou: TESOURA')
else:
    print('Opção inválida!')
if pc == 1:
    print('O computador jogou: PEDRA')
elif pc == 2:
    print('O computador jogou: PAPEL')
elif pc == 3:
    print('O computador jogou: TESOURA')
else:
    print('Opção inválida!')
print('=-='*10)
if jogador == pc:
    print('Resultado: EMPATE!')
elif jogador == 1 and pc == 3:
    print('Resultado: PARABÉNS, VOCÊ GANHOU!')
elif jogador == 3 and pc == 2:
    print('Resultado: PARABÉNS, VOCÊ GANHOU!')
elif jogador == 2 and pc == 1:
    print('Resultado: PARABÉNS, VOCÊ GANHOU!')
else:
    print('Resultado: Você perdeu, tente novamente!')
# primeira forma de fazer
jokenpo = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0, 2)
print('='*10, 'JOKENPO!', '='*10)
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
print('=-='*10)
jogador = int(input('Qual a sua  jogada? '))
sleep(2)
print('JO!')
sleep(2)
print('KEN!!')
sleep(2)
print('PO!!!')
print('=-='*10)
print('O computador escolheu {}'.format(jokenpo[computador]))
print('Você escolheu {}'.format(jokenpo[jogador]))
if computador == 0:
    if jogador == 1:
        print('Parabéns, você ganhou!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Empate!')
elif computador == 1:
    if jogador == 2:
        print('Parabéns, você ganhou!')
    elif jogador == 0:
        print('Você perdeu!')
    else:
        print('Empate!')
elif computador == 2:
    if jogador == 0:
        print('Parabéns, você ganhou!')
    elif jogador == 1:
        print('Você perdeu!')
    else:
        print('Empate!')
else:
    print('Jogada inválida!')
