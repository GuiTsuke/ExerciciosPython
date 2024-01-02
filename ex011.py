altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))
area = altura * largura
tinta = area / 2
print('Com a altura de {}m e largura de {}m, a sua área é de {:.2f}m².\nLogo a quantidade de tinta necessária é de {:.2f}l.'.format(altura, largura, area, tinta))
