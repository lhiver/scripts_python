'''alistamento militar'''
from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'Você tem {idade} anos')
if idade < 18:
    print('Você ainda não pode se alistar no exercito')
elif idade == 18:
    print('Vai se alistar vagabundo')
else:
    print('Você já passou da idade de se alistar')
