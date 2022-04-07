n = str(input('Entre com seu nome completo: ')).strip()
nome = n.split()
print('Seu primeito nome é {}' .format(nome[0]))
print('Seu ultimo nome é {}' .format(nome[len(nome)-1]))

