# escreva um programa que leia o valor em metros e exiba convertido em centimetros e milimetros.
m = float (input ('Digite o valor em metros: '))
cm = m * 100
ml = m * 1000
print('O valor de {} em centimentros é {:.0f}cm enquanto em milimetros é {:.0f}mm'.format(m,cm,ml))