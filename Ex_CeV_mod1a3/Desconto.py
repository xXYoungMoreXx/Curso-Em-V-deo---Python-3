print('='*45)
p = input('Digite o nome do produto: ')
vpp = float(input('Digite o valor padrão do produto: R$'))
des = int(input('Digite o desconto: %'))
vcd = vpp*(des/100)
vfp = vpp - vcd
print('='*45)
print('Este produto está {}% OFF! \n'.format(des), end='')
print('De {}R$ foi para {}R$!!'.format(vpp, vfp))
print('='*45)
