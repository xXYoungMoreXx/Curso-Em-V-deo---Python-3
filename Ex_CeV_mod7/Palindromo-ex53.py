# Crie um programa que leia uma palavra e diga se é um palindromo
phrase = str(input('Digite algo: ')).strip().upper()
words = phrase.split()
noSpace = ''.join(words)
inverse = ''
# o comando '"".join()' serve pra juntar as palavras separadas pelo split
# Enquanto o "inverse" serve para inverter a var Phrase através do proximo for
for letters in range(len(noSpace)-1, -1, -1):
    inverse += noSpace[letters]
if inverse == noSpace:
    print('\033[32mTemos um palindromo!')
else:
    print('\033[31mA frase digitada não é um palindromo!')
