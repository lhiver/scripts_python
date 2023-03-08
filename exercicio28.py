'''jogo da adivinhação'''
from random import randint
from time import sleep
import emoji
n = randint(1, 5)
print('-=-'*20)
print(emoji.emojize('Bem vindo ao jogo da adivinhação :cat_with_wry_smile:\n'))
print('-=-' * 20)
numero = int(input('Adivinhe qual foi o número que o computador pensou: \n'))
print('\33[31mPROCESSANDO...\33[m')
sleep(3)
if numero == n:
    print(emoji.emojize(
        f'\33[32mQue legal vc acertou o número correto era {n}\33[m :thumbs_up:'))
else:
    print(emoji.emojize(
        f'Que pena vc errou o número correto era {n} :thumbs_down:'))
