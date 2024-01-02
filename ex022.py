nome = str(input('Digite seu nome completo: ')).strip()

nome = nome.split()
nome = ' '.join(nome)
print("Seu nome é : {}".format(nome))
print("Letras maiúsculas: {}".format(nome.upper()))
print('Letras minúsculas: {}'.format(nome.lower()))
print('Ao todo sem espaços tem: {} letras'.format(len(nome) - nome.count(' ')))
print('Ao todo sem espaços tem: {} letras'.format(len(nome.replace(' ', ''))))
divi = nome.split()
print('O primeiro nome tem: {} letras'.format(len(divi[0])))
print('O primeiro tem {} letras'.format(nome.find(' ')))



