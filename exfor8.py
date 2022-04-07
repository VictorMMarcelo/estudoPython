frase = str(input('Entre com a frase: ')).strip().upper()
palavras = frase.split()
junto = '' .join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('o inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('Ele é um palindromo')
else:
    print('Ele não é um palindromo!')
