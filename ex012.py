preco = float(input('Qual preço do produto? '))
desconto = (5/100) * preco
nPreco = preco - desconto
print('O preço a pagar é de R${:.2f}.'.format(nPreco))
