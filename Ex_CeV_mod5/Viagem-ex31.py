tr = float(input('quantos KM terá a viagem? '))
if tr > 200:
    print('Valor da passagem: {:.2f}R$'.format(tr*0.45))
else:
    print('Valor da passagem: {:.2f}R$'.format(tr*0.5))
print('Tenha uma ótima viagem!')
