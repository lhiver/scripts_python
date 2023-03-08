# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
import emoji
num = float(input(emoji.emojize('Digite um número :ant: ')))
inteiro = trunc(num)
print(emoji.emojize(f'{inteiro} :wolf:'))
