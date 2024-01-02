salario = float(input('Qual seu atual salário? '))
aumento = (15/100) * salario
nSalario = salario + aumento
print('O seu novo salário é de R${:.2f}.'.format(nSalario))
