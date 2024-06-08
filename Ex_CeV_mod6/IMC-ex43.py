import time
peso = float(input('Qual o seu peso? (KG)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura**2)
print('-=-'*15)
print('Calculando...')
time.sleep(2)
print('-=-'*15)
print('O IMC desta pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Parabéns! seu peso é ideal.')
elif imc <= 30:
    print('Você está com sobrepeso. Procure um nutricionista!')
elif imc <= 40:
    print('Você está em obesidade. Cuidado!')
elif imc > 40:
    print('Você está com obesidade mórbida. Procure ajuda médica!')
