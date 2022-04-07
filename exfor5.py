soma = 0
c = 0
for i in range(1, 7):
    num = int(input('Digite o {} valor:  ' .format(i)))
    if num % 2 == 0:
        soma += num
        c += 1
print(' você informou {} números pares e a soma foi {}' . format(c, soma))