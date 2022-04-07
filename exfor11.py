cid = 0
tots = 0
mhomem = 0
nomev = ''
for i in range(1, 5):
    nome = str(input('insira seu nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    cid += idade
    media = cid / i
    if sexo == 'F':
        if idade < 20:
            tots += 1
    if i == 1 and sexo in 'Mm':
        mhomem = idade
        nomev = nome
    if sexo in 'Mm' and idade > mhomem:
        mhomem = idade
        nomev = nome
print('O homem mais velho tem {} anos e se chama {}.' .format(mhomem, nomev))
print('Quantidade de mulheres menos de 20 anos é {}' .format(tots))
print('A media de idade do grupo é: {}' .format(media))
