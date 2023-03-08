'''verificar se existe silva no nome da pessoa'''
nome = input('Digite um nome: ').strip().lower()
PALAVRA = 'silva'
print(PALAVRA in nome)
