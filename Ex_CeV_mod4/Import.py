import math
# Para importar especificamente uma função ao invés de um módulo inteiro usamos
# from (módulo) import (função)
n1 = float(input('Digite um número para saber a raiz quadrada dele: '))
raiz = math.sqrt(n1)
print('A raiz de {} é {:.2f}'.format(n1, raiz))
