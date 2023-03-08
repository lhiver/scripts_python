'''Encontrar letra a nas palavras'''
frase = input('Digite uma frase: ').strip().lower()
a = frase.count('a')
primeira = frase.find('a')
ultima = frase.rfind('a')
print(f'A letra A aparece {a} vezes')
print(f'A letra A aparece pela primeira vez na posição {primeira}')
print(f'A letra A aparece pela ultima vez na posição {ultima}')
