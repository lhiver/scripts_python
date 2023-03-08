# crie um programa que leia o nome completo de uma pessoa e
# mostre o nome com todas as letras maisculas
# o nome com todas as letras minusculas
# quantas letras ao todo sem considerar espaços
# quantas letras tem o primeiro nome
'''fatiador de nomes'''
nome = input(str('Digite um nome completo: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
letras = len(nome) - nome.count(' ')
primeironome = nome.split()


print(f'O seu nome em maiusculo é {maiusculo}')
print(f'O seu nome em minusculo é {minusculo}')
print(F'O seu nome completo tem {letras} letras')
print(f'O seu primeiro nome é {primeironome[0]} e tem {len(primeironome[0])} letras')
