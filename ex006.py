n = int(input('Digite um número: '))
d2 = n * 2
d3 = n * 3
rz = n ** (1/2)
print('O dobro é {}, \no triplo é {} e \na raiz quadrada é {:.2f}.'.format(d2, d3, rz))
print('Mas para economizar memória, O dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n * 2, n * 3, n ** (1/2)))
print('A função de potencia é pow(n, (1/2)) que dá {:.2f}'.format(pow(n, (1/2))))
