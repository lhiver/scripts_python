'''formando retas'''
reta1 = int(input('Digite o valor da reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('podem formar um triangulo')
else:
    print('Não podem formar um triangulo')
