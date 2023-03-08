# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
c_oposto = float(input('Digite o valor do cateto oposto: '))
c_adjacente = float(input('Digite o valor do cateto adjacente: '))
resultado = (c_oposto * c_oposto) + (c_adjacente * c_adjacente)
hipotenusa = sqrt(resultado)
print('valor da hipotenusa é  {}'.format(hipotenusa))
