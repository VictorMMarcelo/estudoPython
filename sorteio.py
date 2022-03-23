import random
n1 = str(input('primeiro numero'))
n2 = str(input('segundo numero'))
n3 = str(input('terceio numero'))
n4 = str(input('quarto numero'))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('aluno escolhido foi {}' .format(escolhido))
