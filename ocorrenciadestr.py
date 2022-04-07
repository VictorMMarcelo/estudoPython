frase = str(input('Entre com seu numero')).upper().strip()
print('A letra A aparece {} vezes na frase' .format(frase.count('A')))
print('A primeira Letra A apareceu na posição {}' .format(frase.find('A')+1))
print('A ultima letra A apareceu no posição {}' .format(frase.rfind('A')+1))

