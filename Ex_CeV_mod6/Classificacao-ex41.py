from datetime import date
import time
nascimento = int(input('Em que ano nasceu?'))
atual = date.today().year
idade = atual - nascimento
print('-=-'*15)
print('Aguarde...')
time.sleep(2)
print('-=-'*15)
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('classificação: Mirim')
elif idade <= 14:
    print('classificação: Infantil')
elif idade <= 19:
    print('classificação: Júnior')
elif idade <= 25:
    print('classificaçâo: Sênior')
else:
    print('classificaçâo: Master')
