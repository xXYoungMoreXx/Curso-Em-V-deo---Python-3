from datetime import date
y1 = int(input('Diga um ano (Digite "0" para analisar o ano atual): '))
if y1 == 0:
    y1 = date.today().year
if y1 % 4 == 0 and y1 % 100 != 0 or y1 % 400 == 0:
    print('O ano {} é bissexto!'.format(y1))
else:
    print('O ano {} não é bissexto'.format(y1))
