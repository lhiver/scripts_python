'''fogos de artificio'''
from time import sleep
from emoji import emojize


for n in range(10, 0, -1):
    print(n)
    sleep(1)
print('\033[33mFELIZ ANO NOVO!!!\033[m')
print(emojize(':fireworks: :fireworks: :fireworks:'))
