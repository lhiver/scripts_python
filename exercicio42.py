'''Triangulos'''
reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('podem formar um triangulo')
    if reta1 == reta2 == reta3:
        print('Equilátero')
    if reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Isósceles')
    if reta1 != reta2 != reta3 != reta1:
        print('Escaleno')
else:
    print('Não pode formar um triangulo')
