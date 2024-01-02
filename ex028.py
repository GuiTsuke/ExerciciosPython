import random
from time import sleep
print('Vamos começar!... Pensei num número, advinhe!')
n2 = random.randint(0,5)
n1 = int(input('Qual número que o PC pensou? '))
print('Verificando...')
sleep(2)
print('Acertou' if n1 == n2 else 'Errou')
print('O computador pensou em: {}'.format(n2))
