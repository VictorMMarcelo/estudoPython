vl = float(input('Entre com a velocidade: '))
if vl <= 80:
    print('Você não foi mutado')
else:
    m = (vl-80)*7
    print('Você foi multado por {:.2}' .format(m))
print('Dirija com cuiado')
