# Escreva um programa que leia nome, idade e sexo de 4 pessoas
# No final mostre:
# Qual a média de idade do grupo, qual o nome do homem mais velho
# E quantas mulheres tem menos que 20 anos
contwom = 0
somage = 0
oldagemen = 0
agewoman = 0
oldmename = ''
print("\033[32m-="*7, "ANÁLISADOR", "=-"*7)
pessoas = int(input("\033[mQuantas pessoas pretende analisar? "))
for c in range(1, pessoas+1):
    print("\033[32m-="*7, "{}° ANÁLISE".format(c), "=-"*7)
    nome = input("\033[mQual o nome da {}° pessoa? ".format(c)).strip().title()
    idade = int(input("idade? "))
    sexo = str(input("sexo?\033[32m[M / F] ")).strip().upper()
    if sexo == "F" and idade < 20:
        contwom += 1
    if c == 1 and sexo == "M":
        oldagemen = idade
        oldmename = nome
    if sexo == 'M' and idade > oldagemen:
        oldagemen = idade
        oldmename = nome
    somage += idade
print("-="*7, "RESULTADO", "=-"*7)
media = int(somage / pessoas)
print("\033[mO homem mais velho do grupo é: \033[32m{}".format(oldmename))
print("\033[mA media de idade dessas pessoas é: \033[32m{}".format(media))
print("\033[mTotal de mulheres menores de 20 anos é: {}".format(contwom))
