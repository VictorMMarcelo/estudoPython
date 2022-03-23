import random
import numpy as np
qdt = maior = menor = 0
n1 = np.random.randint(0,101, size=30)
print(n1)

print('')

for i in n1:
    if i % 2 == 0:
        print('Valor par {}'.format(i))

print('')

for i in n1:
    if qdt == 1:
        maior = menor = i
    else:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    qdt += 1
print('maior {} e menor {}' .format(maior, menor))

print('')


for i in n1:
    if i > 50:
        print('Numero maior que 50: {}' .format(i))
