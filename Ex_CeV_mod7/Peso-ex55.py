# Faça um programa que leia o peso de cinco pessoas
# No final mostre qual foi o menor e o maior
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input("Qual o peso da {}° pessoa? ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print("o maior peso foi \033[31m{:2}\033[mKg".format(maior))
print("O menor peso foi \033[36m{:2}\033[mKg".format(menor))
