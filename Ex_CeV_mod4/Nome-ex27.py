name = str(input('Digite um nome: ')).strip()
firstn = name.split()
ls = name.rfind(' ')
lastn = (name[ls:])
print('O primeiro nome é: {}'.format(firstn[0]))
print('O último nome é:{}'.format(lastn))
