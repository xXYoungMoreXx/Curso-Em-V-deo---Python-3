car = int(input('O veículo estava a quantos KM/H? '))
if car <= 80:
    print('Tenha um ótimo dia e aproveite a viagem!')
else:
    print('MULTADO! você excedeu o limite permitido de 80KM/H.')
tt = (car-80)*7
print('Valor da multa: {}R$'.format(tt))
