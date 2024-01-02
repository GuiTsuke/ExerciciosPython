from math import sin, cos, tan, radians
print('Calcular Seno, Cosseno e Tangente do Ângulo')
num = float(input('Digite um Ângulo: '))
rad = radians(num)
print('O ângulo digitado foi {:.0f} e em radiano {:.2f}.'.format(num, rad))
print('O seno é aproximadamente {:.2f} '.format(sin(rad)))
print('O cosseno é aproximadamente {:.2f}'.format(cos(rad)))
print('A tangente é aproximadamente {:.2f}'.format(tan(rad)))
