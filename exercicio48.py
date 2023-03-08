'''soma de numeros multiplos de 3'''
soma = 0
contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        contador = contador + 1
print(f"No total foram somados {contador} números")
print(f'A soma de todos os valores é {soma}')
