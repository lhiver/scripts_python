# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float (input('Digite o preço original do produto: '))
desconto = produto - (produto * 5 / 100)
print('O preço do produto é {} e com o desconto de 5% fica {} '.format(produto, desconto))


