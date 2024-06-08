t1 = int(input('Digite o primeiro termo: '))
# Primeiro Termo
ra = int(input('Digite a razão: '))
# Razão
dec = t1 + (10-1) * ra
# Fómula para chegar até o décimo termo = 9 * ra + t1
for n in range(t1, dec + ra, ra):
    print(n, end=" -> ")
print('Fim da progressão!')
