# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
alunos = ['rodrigo', 'lucas', 'luciano', 'gabriel']
print('\nLista de alunos\n')
print(alunos)
shuffle(alunos)
print('\nOrdem dos alunos que vão apagar o quadro:\n')
print(alunos)
