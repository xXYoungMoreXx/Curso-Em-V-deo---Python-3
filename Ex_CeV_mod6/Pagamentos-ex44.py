print("="*15, "More's Store", '='*15)
valor = float(input('Qual o valor da compra? R$'))
print('=-'*25)
print("""[ 1 ] á vista
[ 2 ] Débito
[ 3 ] crédito até 2x sem juros!
[ 4 ] crédito de 3x a 10x com juros!""")
print('=-'*25)
metodo = int(input('Escolha o método de pagamento: '))
print('=-'*25)
if metodo == 1:
    print('Sua compra de {:.1f}R$ recebeu um desconto de 10%!'.format(valor))
    print('O total ficou: {:.1f}R$'.format(valor - (valor * 10 / 100)))
elif metodo == 2:
    print('Sua compra de {:.1f}R$ recebeu um desconto de 5%!'.format(valor))
    print('O valor final é {:.1f}R$'.format(valor - (valor * 5 / 100)))
elif metodo == 3:
    parcelas = int(input('Quantas parcelas? x'))
    print('=-'*25)
    if parcelas == 1:
        print('O valor das parcelas será: {:.1f}R$'.format(valor))
    elif parcelas == 2:
        print('O valor das parcelas será: {:.1f}R$'.format(valor / 2))
    else:
        print('Opção inválida!')
elif metodo == 4:
    parcelas = int(input('Quantas parcelas? x'))
    print('=-'*25)
    juros = valor + (valor * 20 / 100)
    if parcelas >= 3 and parcelas <= 10:
        print('O valor das parcelas será: {:.1f}R$'.format(juros / parcelas))
        print('O valor total será: {:.1f}'.format(juros))
    else:
        print('Opção inválida!')
else:
    print('Opção inválida!')
