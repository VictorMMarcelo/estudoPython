km = int(input('Entre com a distancia: '))
if km <= 200:
    r1 = km * 0.50
    print('Valor a pagar na viagem: {}R$' .format(r1))
else:
    r2 = km * 0.45
    print('Valor a pagar na viagem longa: {}R$' .format(r2))
