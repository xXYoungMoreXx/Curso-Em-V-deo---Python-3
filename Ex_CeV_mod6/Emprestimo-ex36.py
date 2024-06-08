import time
print('-=-'*10)
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu sálario? R$'))
emprestimo = int(input('Em quantos anos pretende quitar? '))
print('-=-'*10)
print('Aguarde, estamos analisando suas informações...')
time.sleep(2)
parcela = casa / (emprestimo * 12)
if parcela <= (salario * 30 / 100):
    print('Seu empréstimo foi aprovado!')
else:
    print('Infelizmente não podemos aprovar seu empréstimo no momento.')
print('As parcelas ficam por: {:.2f}'.format(parcela))
