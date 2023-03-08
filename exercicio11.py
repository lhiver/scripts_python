# faça um programa que leia a largura e altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta nescessária
# para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2
largura = float (input ('Digite a largura da parede: '))
altura = float (input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('A area da parede é de {:.2f}m2 quadrados e a quantidade nescessaria de tinta para pintar essa area é de  {:.1f}LT de tinta'
      ''.format(area, tinta))

