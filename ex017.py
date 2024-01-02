from math import hypot, sqrt, pow
print('Calculo da Hipotenusa do Triângulo Retângulo')
num = float(input('Comprimento do Cateto Oposto: '))
num2 = float(input('Comprimento do Cateto Adjascente: '))
num3 = hypot(num, num2)
num4 = (sqrt(pow(num, 2) + pow(num2, 2)))
num5 = (num ** 2 + num2 ** 2) ** (1/2)
print('A Hipotenusa é: {:.2f}'.format(num3))
print('A Hipotenusa também é: {:.2f}'.format(num4))
print('A Hipotenusa também é: {:.2f}'.format(num5))



