print('-='*20)
s1 = input('Digite o valor do seguimento 1: ')
s2 = input('Digite o valor do seguimento 2: ')
s3 = input('Digite o valor do seguimento 3: ')
print('-='*20)
if s1 + s2 < s3 and s2 + s3 < s1 and s1 + s3 < s2:
    print('Sim! esses 3 segmentos podem virar um triângulo.')
else:
    print('Não! esses 3 segmentos não podem virar um triângulo.')
