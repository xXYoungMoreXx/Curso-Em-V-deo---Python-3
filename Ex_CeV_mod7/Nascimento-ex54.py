# Crie um programa que leia o ano de nascimento de 7 pessoas
from datetime import date
# No final mostre quantos não atingiram a maioridade e quantos já
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Digite em que ano a {}° pessoa nasceu: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('''São \033[32m{}\033[m pessoas maiores de idade 
E somente \033[36m{}\033[m menores.'''.format(maior, menor))
