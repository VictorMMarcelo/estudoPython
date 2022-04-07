from datetime import date
totm = 0
tota = 0
atual = date.today().year
for i in range(1, 8):
    ano = int(input('Entre com o ano de nascimento: '))
    idade = atual - ano
    if idade >= 18:
        tota += 1
    else:
        totm += 1
print('Já são menores  de idade {}'.format(totm))
print('Já são maiores de idade {}' .format(tota))
