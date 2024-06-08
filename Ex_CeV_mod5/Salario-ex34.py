payment = float(input('Digite o valor do salário: R$'))
sup10 = payment + (payment * 10 / 100)
sup15 = payment + (payment * 15 / 100)
if payment > 1250:
    print('Parabéns, você acaba de receber um aumento para {}'.format(sup10))
else:
    print('Parabéns, você acaba de receber um aumento para {}'.format(sup15))
