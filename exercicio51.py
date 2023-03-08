a = int(input('Digite o 1° termo: '))
r = int(input('Digite a razão: '))
decimo = a +(11 - 1) * r
for c in range(a,decimo,r):
    resultado = a + r
    print(f'{c} ', end='')    
