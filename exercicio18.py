'''calculo seno,cosseno,tangente'''
from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O valor do seno é {seno:.2f}\n')
print(f'\nO valor do cosseno é {cosseno:.2f}\n')
print(f'\nO valor da tangente é {tangente:.2f}')
