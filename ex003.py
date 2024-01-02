n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
cores = {'red': '\033[1;31m', 'green': '\033[1;32m', 'limpa': '\033[m'}
print("A soma entre {}{}{} e {}{}{} é igual a {}{}{}".format(cores['red'], n1, cores['limpa'], cores['red'], n2,
                                                             cores['limpa'], cores['green'], s, cores['limpa']))
