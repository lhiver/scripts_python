n = int(input('Digite um número: '))
total = 0
for c in range (1,n+1):
    if n % c == 0:
        print('\033[32m', end='')
        total += 1  
    else:
        print('\033[31m', end ='')
    print(f'{c} ', end='')    
print(f'\n\033[mO número {n} foi divido {total} vezes')    
if total <=2:
    print(f'\033[32mO número {n} é primo\033[m')
else:
    print(f'\033[35mO número {n} não é primo\033[m')