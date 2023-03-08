'''pedra,papel e tesoura'''
from random import choice
from time import sleep
print('Bem vindo ao jokenpo')
print('Escolha entre pedra, papel ou tesoura')
jokenpo = ['pedra', 'papel', 'tesoura']
vc = input('Digite a sua escolha: ')
pc = choice(jokenpo)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print(f'\033[31mO pc escolheu {pc}\033[m')
print(f'\033[32mVocê escolheu {vc}\033[m')

if pc == 'pedra' and vc == 'tesoura':
    print('O pc venceu')
elif vc == 'pedra' and pc == 'tesoura':
    print('Vc venceu')

elif pc == 'papel' and vc == 'pedra':
    print('O pc venceu')
elif vc == 'papel' and pc == 'pedra':
    print('vc ganhou')

elif pc == 'tesoura' and vc == 'papel':
    print('O pc venceu')
elif vc == 'tesoura' and pc == 'papel':
    print('vc venceu')
elif vc == 'tesoura' and pc == 'tesoura' or vc == 'pedra' and pc == 'pedra':
    print('Empate')
elif vc == 'papel' and pc == 'papel':
    print('Empate')
else:
    print('\033[31mOpção invalida\033[m')
