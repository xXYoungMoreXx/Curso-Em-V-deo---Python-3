fr = str(input('Digite uma frase: ')).strip().upper()
# fr = Frase
print('Na frase, tem {} Letra "A"'.format(fr.count('A')))
pla = fr.find('A')
# pla = Primeira letra "A"
epa = fr.count(' ', 0, pla)
# epa = Quantidade de espaço em branco antes da primeira letra "A"
ula = fr.rfind('A')
# ula =  Última letra "A"
eua = fr.count(' ', 0, ula)
# eua = Quantidade de espaço em branco após a última letra "A"
print('A primeira letra "A" aparece como {}° letra'.format(fr.find('A')+1-epa))
print('A última letra "A" aparece como {}° letra'.format(fr.rfind('A')+1-eua))
