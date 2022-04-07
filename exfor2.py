s = 0
c = 0
for i in range(1, 500+1, 2):
    if i % 3 == 0:
        c += 1
        s += i
print('somatoria dos valores {} solicitados é {}' .format(c, s))


