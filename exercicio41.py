'''natação'''
from datetime import date
atleta = int(input('Em que ano você nasceu? '))
categoria = date.today().year - atleta
print(f'Você tem {categoria} anos')
if categoria <= 9:
    print('Sua categoria é mirim')
elif categoria > 9 and categoria <= 14:
    print('Sua categoria é infantil')
elif categoria > 14 and categoria <= 19:
    print('Sua categoria é junior')
elif categoria == 20:
    print('Sua categoria é senior')
else:
    print('Sua categoria é master')
