larg = float( input('Entre com a Largura da parede'))
alt = float( input('Entre com a altura da parede'))
area = alt*larg
print('Sua parede tem a dimensão de {}X{} e sua area é de {}m².' .format(larg, alt, area))
tinta = area/2
print('Para pintar essa parede, você precirá de {}l de tinta' .format(tinta))


