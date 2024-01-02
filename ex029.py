print('RADAR ELETRÔNICO!!!')
v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Ei, você acaba de ser multado por excesso de velocidade!')
    vm = (v - 80) * 7
    print('Sua velocidade era de {}Km/h, por isso vai pagar R${:.2f}'.format(v, vm))
else:
    print('Tudo normal por aqui!')