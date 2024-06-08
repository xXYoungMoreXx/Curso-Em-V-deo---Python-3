print('='*50)
alt = float(input('Digite a altura? '))
lar = float(input('Digite a largura? '))
ar = alt*lar
ti = ar/2
print('='*50)
print('A Área mede {}m²\n'.format(ar), end='')
print('Para pintar a área você irá utilizar: {:.2f}L de tinta'.format(ti))
print('='*50)
