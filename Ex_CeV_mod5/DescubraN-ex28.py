import random
import time
n1 = random.randint(0, 5)
print('-=-'*15)
n2 = int(input('Tente adivinhar o número secreto: '))
print('-=-'*15)
print('Analisando...')
time.sleep(2)
print('-=-'*15)
if n2 == n1:
    print('PARABÉNS!!! Você acertou o número')
else:
    print('Você errou. O número correto era: {}'.format(n1))
print('-=-'*15)
print('Tente Novamente!')
print('-=-'*15)
