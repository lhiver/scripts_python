'''dividindo numero em unidade,dezena,centena e milhar'''
n = int(input('Digite um número: '))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print(f'Unidade = {unidade}')
print(f'Dezena = {dezena}')
print(f'Centena = {centena}')
print(f'Milhar = {milhar}')
