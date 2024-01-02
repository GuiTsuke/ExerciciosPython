n = float(input('Quantos reais você quer converter em dolar? R$'))
dol1 = n / 3.27
dol2 = n / 5.10
print('R${:.2f} poderia ser trocado em 2016 por em torno de ${:.2f} \nJá em 2022 por aproximadamente ${:.2f}'.format(n, dol1, dol2))
