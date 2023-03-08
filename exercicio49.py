''''tabuada parte 2'''
n = int(input('Digite um numero entre 1 e 10: '))
for tabuada in range(0, 11):
    mult = n * tabuada
    print(f'{n} x {tabuada} = {mult}')
