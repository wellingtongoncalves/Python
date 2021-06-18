larg = float(input('Qual é a largura da parede: '))
alt = float(input('Qual é a altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m. '.format(larg,alt,area))
quan_tint = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(quan_tint))
