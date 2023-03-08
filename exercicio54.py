maior = 0
menor = 0
for c in range(1,8):
    data_nasc = int(input('Digite a data de nascimento: '))
    if data_nasc < 2005:
        maior += 1
    else:
        menor +=1    
print(f'Existem {maior} pessoas maiores de idade e {menor} menores')        
