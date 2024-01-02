print('AUMENTO DE SALARIO')
s = float(input('Digite seu salário:'))
if s > 1250:
    novo = s + (10 / 100 * s)
    print('Seu salário de R${:.2f} teve um aumento de 10%, valor atual: R${:.2f}'.format(s, novo))
else:
    novo = s + (15 / 100 * s)
    print('Seu salário de R${:.2f} teve um aumento de 15%, valor atual: R${:.2f}'.format(s, novo))
