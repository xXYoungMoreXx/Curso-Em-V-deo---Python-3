from datetime import date
nasceu = int(input('Digite o ano em que nasceu: '))
atual = date.today().year
idade = atual - nasceu
print('-=-'*15)
print('Se você nasceu em {}, sua idade é de {} anos.'.format(nasceu, idade))
print('-=-'*15)
if idade < 18:
    print('Você ainda não completou 18 anos.')
    print('Deverá se alistar em {}.'.format(atual + (18 - idade)))
elif idade > 18:
    print('Você deveria ter se alistado a {} anos.'.format(idade - 18))
    print('Procure o quartel mais próximo com urgência!')
else:
    print('Você completou 18 anos e deve se apresentar num quartel próximo!')
