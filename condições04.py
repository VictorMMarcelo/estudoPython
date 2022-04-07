import random

n = random.randint(0, 5)
n1 = int (input('Adivinhe o nemero de 0 a 5:'))
if n == n1:
    print('Você adivinhou o numero.')
else:
    print('Você não adivinhou o numero que pensei {}.' .format(n))
print('fim')
