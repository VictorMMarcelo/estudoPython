#10 termos de uma PA
n = int(input('Insire o primeiro numero: '))
r = int(input('insira a razão: '))
decimo = n + (10-1) * r
for i in range(n, decimo + r, r):
    print('{} ' .format(i), end='-> ')
print('Acabou')
