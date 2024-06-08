acum = 0
cont = 0
for n in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        acum += n
        # Acumulador
        cont += 1
        # Contador
print(acum)
