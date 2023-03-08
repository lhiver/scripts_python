'''carro e aluguel'''
km = float(input('Digite um valor em KM: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
preco = dias * 60 + (km * 0.15)
print(f'Em {dias} dias e por {km} KM rodados o preço ficou {preco} reais')
