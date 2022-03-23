dias = int(input('Entre com dias do aluguel:'))
km = float(input('Entre com o km:'))
resuld = dias*60
resultkm = km*0.15
result = resuld+resultkm
print('Total a pagar R${:.2f}' .format(result))